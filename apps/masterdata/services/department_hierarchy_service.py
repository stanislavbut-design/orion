# apps/masterdata/services/department_hierarchy_service.py

from django.core.exceptions import ValidationError
from django.db import transaction

from collections import deque

from apps.masterdata.models import (
    Department,
    Party,
    ResponsibilityCenter,
)

from apps.core.constants.validation.masterdata import (
    DEP_PARENT_SELF_ERROR,
    DEP_ROOT_COMPANY_ONLY_ERROR,
    DEP_CIRCULAR_HIERARCHY_ERROR,
    DEP_ORPHANED_DEPARTMENT_ERROR,
    DEP_RC_OVERRIDE_ERROR,
    DEP_RC_MUST_BE_LEAF_ERROR,
)


class DepartmentHierarchyService:
    """
    Maintains Department hierarchy and inherited structural attributes.
    """

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    @staticmethod
    @transaction.atomic
    def initialize(department: Department):
        """
        Initialize a new Department and its hierarchy attributes.
        """

        if department.parent_department is None and department.company is None:
            raise ValidationError(
                DEP_ORPHANED_DEPARTMENT_ERROR
            )

        department.save()

        if department.parent_department is None:
            department.root_department = department
        else:
            department.company = department.parent_department.company
            department.responsibility_center = department.parent_department.responsibility_center
            department.root_department = DepartmentHierarchyService._root_department(department.parent_department)

        department.save(update_fields=["root_department", "company", "responsibility_center"])

    @staticmethod
    @transaction.atomic
    def apply_update(
        original: Department,
        edited: Department,
    ):
        """
        Apply changes to a Department and propagate inherited hierarchy attributes.
        """
        parent_changed = original.parent_department_id != edited.parent_department_id
        company_changed = original.company_id != edited.company_id
        rc_changed = original.responsibility_center_id != edited.responsibility_center_id

        hierarchy_changed = (
            parent_changed
            or company_changed
            or rc_changed
        )

        if hierarchy_changed: 

            # DEP-008 — Department Company Association
            if edited.parent_department is None and edited.company is None:
                raise ValidationError(
                    DEP_ORPHANED_DEPARTMENT_ERROR
                )  

            if parent_changed:

                DepartmentHierarchyService.change_parent(
                    edited,
                    edited.parent_department,
                    edited.company,
                )

            if company_changed:

                DepartmentHierarchyService.assign_company(
                    edited,
                    edited.company,
                )

            if rc_changed:

                # DEP-011 — Responsibility Center Association
                if edited.parent_department is not None and edited.responsibility_center != edited.parent_department.responsibility_center:
                    raise ValidationError(
                        DEP_RC_OVERRIDE_ERROR
                    )
                
                # RCN-009 — Direct Association Target, RCN-011 — No Lower-Level Override
                if edited.responsibility_center is not None and not edited.responsibility_center.is_leaf:
                    raise ValidationError(
                        DEP_RC_MUST_BE_LEAF_ERROR
                    )

                DepartmentHierarchyService.assign_responsibility_center(
                    edited,
                    edited.responsibility_center,
                )

        edited.save()


    @staticmethod
    def assign_company(department: Department, company: Party):
        """
        Assign a Company to a root Department and propagate it
        throughout its subtree.
        """

        if department.parent_department is not None:
            raise ValidationError(
                DEP_ROOT_COMPANY_ONLY_ERROR
            )

        DepartmentHierarchyService._propagate_company(
            department,
            company,
        )

    @staticmethod
    def assign_responsibility_center(
        department: Department,
        responsibility_center: ResponsibilityCenter,
    ):
        """
        Assign a Responsibility Center to a Department and propagate it
        throughout its subtree.
        """

        DepartmentHierarchyService._propagate_responsibility_center(
            department,
            responsibility_center,
        )

    @staticmethod
    def change_parent(
        department: Department,
        new_parent: Department,
        new_company: Party | None = None,
    ):
        """
        Change a Department's parent and propagate inherited hierarchy attributes.
        """

        if department == new_parent:
            raise ValidationError(DEP_PARENT_SELF_ERROR)

        if new_parent in DepartmentHierarchyService._subtree(department):
            raise ValidationError(
                DEP_CIRCULAR_HIERARCHY_ERROR
            )

        department.parent_department = new_parent

        if new_parent is not None:
            department.root_department = new_parent.root_department

            department.save(update_fields=[
                "parent_department",
                "root_department",
            ])

            DepartmentHierarchyService._propagate_company(
                department,
                new_parent.company,
            )

            DepartmentHierarchyService._propagate_responsibility_center(
                department,
                new_parent.responsibility_center,
            )

        else:
            department.root_department = department

            department.save(update_fields=[
                "parent_department",
                "root_department",
            ])

            DepartmentHierarchyService._propagate_company(
                department,
                new_company,
            )

            DepartmentHierarchyService._propagate_responsibility_center(
                department,
                department.responsibility_center,
            )

        DepartmentHierarchyService._propagate_root_department(
            department,
            department.root_department
        )


    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _propagate_company(
        root: Department, 
        company: Party | None,
    ):

        for department in DepartmentHierarchyService._subtree(root):
            department.company = company
            department.save(update_fields=["company"])

    @staticmethod
    def _propagate_responsibility_center(
        root: Department,
        responsibility_center: ResponsibilityCenter | None,
    ):

        for department in DepartmentHierarchyService._subtree(root):
            department.responsibility_center = responsibility_center
            department.save(update_fields=["responsibility_center"])

    @staticmethod
    def _propagate_root_department(
        root: Department,
        root_department: Department,
    ):

        for department in DepartmentHierarchyService._subtree(root):
            department.root_department = root_department
            department.save(update_fields=["root_department"])  

    @staticmethod
    def _subtree(root: Department):
        """
        Iterates over all Departments in a subtree.
        """

        queue = deque([root])

        while queue:
            department = queue.popleft()
            yield department

            queue.extend(
                Department.objects.filter(
                    parent_department=department
                ).order_by("id")
            )

    @staticmethod
    def _root_department(department: Department):
        """
        Returns the top-most Department in the hierarchy.
        """
        while department.parent_department is not None:
            department = department.parent_department

        return department
