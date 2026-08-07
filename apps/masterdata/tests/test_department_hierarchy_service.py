from django.test import TestCase
from django.core.exceptions import ValidationError

from apps.masterdata.models import (
    Department,
    Party,
    ResponsibilityCenter,
)

from apps.masterdata.services.department_hierarchy_service import (
    DepartmentHierarchyService,
)

from apps.core.constants.validation.masterdata import (
    DEP_CIRCULAR_HIERARCHY_ERROR,
    DEP_ROOT_COMPANY_ONLY_ERROR,
    DEP_RC_MUST_BE_LEAF_ERROR,
    DEP_RC_OVERRIDE_ERROR,
    DEP_ORPHANED_DEPARTMENT_ERROR,
)

from .factories import MasterDataFactoryMixin


class DepartmentHierarchyServiceTests(MasterDataFactoryMixin, TestCase):

    def test_initialize_root_department(self):

        company = self.create_company(
            name="ACME Ltd",
        )

        department = self.create_department(
            name="Finance",
            company=company,
        )

        self.assertEqual(department.company, company)
        self.assertEqual(department.root_department, department)
        self.assertIsNone(department.parent_department)


    def test_initialize_child_department(self):

        company = self.create_company(
            name="ACME Ltd",      
        )

        finance_department = self.create_department(
            name="Finance",
            company=company,
        )

        accounts_payable_department = self.create_department(
            name="Accounts Payable",
            parent=finance_department,
        )

        self.assertIs(accounts_payable_department.root_department, finance_department.root_department)
        self.assertIs(accounts_payable_department.company, finance_department.company)
        self.assertIs(accounts_payable_department.company, company)
        self.assertIsNone(accounts_payable_department.responsibility_center)

    def test_assign_company_propagates(self):

        company = self.create_company(
            name="ACME Ltd",
        )

        finance_department = self.create_department(
            name="Finance",
            company=company,
        )

        accounts_department = self.create_department(
            name="Accounts",
            parent=finance_department,
        )

        accounts_receivable_department = self.create_department(
            name="Accounts Receivable",
            parent=accounts_department,
        )

        self.assertIs(accounts_receivable_department.company, company)
        self.assertIs(accounts_department.company, company)
        self.assertIs(finance_department.company, company)

    def test_change_parent_propagates_new_inherited_attributes(self):

        company = self.create_company(
            name="ACME Ltd",
        )

        responsibility_center = self.create_responsibility_center(
            name="Finance RC",
        )

        finance_department = self.create_department(
            name="Finance",
            company=company,
            responsibility_center=responsibility_center,
        )

        accounts_department = self.create_department(
            name="Accounts",
            parent=finance_department,
        )

        new_company = self.create_company(
            name="NewCo Ltd",
        )

        new_responsibility_center = self.create_responsibility_center(
            name="Sales RC",
        )

        new_parent_department = self.create_department(
            name="NewCo Sales Department",
            company=new_company,
            responsibility_center=new_responsibility_center,
        )

        original = Department.objects.get(pk=accounts_department.pk)
        edited = Department.objects.get(pk=accounts_department.pk)
        edited.parent_department = new_parent_department

        DepartmentHierarchyService.apply_update(
            original=original,
            edited=edited,
        )

        accounts_department.refresh_from_db()

        self.assertEqual(accounts_department.company, new_company)
        self.assertEqual(accounts_department.parent_department, new_parent_department)
        self.assertEqual(accounts_department.responsibility_center, new_responsibility_center)
        self.assertEqual(accounts_department.root_department, new_parent_department.root_department)
        self.assertEqual(finance_department.company, company)
        self.assertEqual(finance_department.responsibility_center, responsibility_center)

    def test_circular_parent_assignment_raises_validation_error(self):

        company = self.create_company(
            name="ACME Ltd",
        )

        finance_department = self.create_department(
            name="Finance",
            company=company,
        )

        accounts_department = self.create_department(
            name="Accounts",
            parent=finance_department,
        )

        accounts_payable_department = self.create_department(
            name="Accounts Payable",
            parent=accounts_department,
        )

        original = Department.objects.get(pk=finance_department.pk)
        edited = Department.objects.get(pk=finance_department.pk)
        edited.parent_department = accounts_payable_department

        with self.assertRaises(ValidationError) as cm:
            DepartmentHierarchyService.apply_update(
                original=original,
                edited=edited,
            )

        self.assertIn(
            DEP_CIRCULAR_HIERARCHY_ERROR,
            cm.exception.messages,
        )

    def test_child_department_cannot_be_assigned_company(self):

        company = self.create_company(
            name="ACME Ltd",
        )

        finance_department = self.create_department(
            name="Finance",
            company=company,
        )

        accounts_department = self.create_department(
            name="Accounts",
            parent=finance_department,
        )

        new_company = self.create_company(
            name="NewCo Ltd",
        )

        original = Department.objects.get(pk=accounts_department.pk)
        edited = Department.objects.get(pk=accounts_department.pk)
        edited.company = new_company

        accounts_department.refresh_from_db()

        self.assertEqual(
            accounts_department.company,
            company,
        )

        with self.assertRaises(ValidationError) as cm:
            DepartmentHierarchyService.apply_update(
                original=original,
                edited=edited,
            )

        self.assertIn(
            DEP_ROOT_COMPANY_ONLY_ERROR,
            cm.exception.messages,
        )

    def test_root_responsibility_center_propagates_to_children(self):

        company = self.create_company(
            name="ACME Ltd",
        )

        finance_department = self.create_department(
            name="Finance",
            company=company,
        )

        accounts_department = self.create_department(
            name="Accounts",
            parent=finance_department,
        )

        accounts_payable_department = self.create_department(
            name="Accounts Payable",
            parent=accounts_department,
        )

        responsibility_center = self.create_responsibility_center(
            name="Finance RC",
        )

        original = Department.objects.get(pk=finance_department.pk)
        edited = Department.objects.get(pk=finance_department.pk)
        edited.responsibility_center = responsibility_center

        DepartmentHierarchyService.apply_update(
            original=original,
            edited=edited,
        )

        finance_department.refresh_from_db()
        accounts_department.refresh_from_db()
        accounts_payable_department.refresh_from_db()

        self.assertEqual(accounts_department.responsibility_center, responsibility_center)
        self.assertEqual(accounts_payable_department.responsibility_center, responsibility_center)
        self.assertEqual(finance_department.responsibility_center, responsibility_center)
        self.assertEqual(accounts_department.company, company)
        self.assertEqual(accounts_payable_department.company, company)   

    def test_responsibility_center_must_be_leaf(self):

        company = self.create_company(
            name="ACME Ltd",
        )

        finance_department = self.create_department(
            name="Finance",
            company=company,
        )

        parent_responsibility_center = self.create_responsibility_center(
            name="Finance RC",
        )

        child_responsibility_center = self.create_responsibility_center(
            name="Accounts RC",
            parent=parent_responsibility_center,
        )

        original = Department.objects.get(pk=finance_department.pk)
        edited = Department.objects.get(pk=finance_department.pk)
        edited.responsibility_center = parent_responsibility_center

        with self.assertRaises(ValidationError) as cm:
            DepartmentHierarchyService.apply_update(
                original=original,
                edited=edited,
            )

        self.assertIn(
            DEP_RC_MUST_BE_LEAF_ERROR,
            cm.exception.messages,
        )

        finance_department.refresh_from_db()

        self.assertEqual(finance_department.company, company)
        self.assertIsNone(finance_department.responsibility_center)

    def test_responsibility_center_cannot_override_parent(self):

        company = self.create_company(
            name="ACME Ltd",
        )

        old_responsibility_center = self.create_responsibility_center(
            name="Finance RC",
        )

        new_responsibility_center = self.create_responsibility_center(
            name="Accounts RC",
        )

        parent_department = self.create_department(
            name="Finance",
            company=company,
            responsibility_center=old_responsibility_center,
        )

        child_department = self.create_department(
            name="Accounts",
            parent=parent_department,
            company=company,
            responsibility_center=old_responsibility_center,
        )

        original = Department.objects.get(pk=child_department.pk)
        edited = Department.objects.get(pk=child_department.pk)
        edited.responsibility_center = new_responsibility_center

        with self.assertRaises(ValidationError) as cm:
            DepartmentHierarchyService.apply_update(
                original=original,
                edited=edited,
            )

        self.assertIn(
            DEP_RC_OVERRIDE_ERROR,
            cm.exception.messages,
        )

        child_department.refresh_from_db()
        parent_department.refresh_from_db()

        self.assertEqual(child_department.company, company)
        self.assertEqual(child_department.parent_department, parent_department)
        self.assertEqual(
            child_department.responsibility_center,
            old_responsibility_center,
        )
        self.assertEqual(parent_department.responsibility_center, old_responsibility_center)        
        self.assertEqual(
            child_department.parent_department,
            parent_department,
        )    

    def test_department_cannot_be_orphan_at_creation(self):

        with self.assertRaises(ValidationError) as cm:
            self.create_department(
                name="Orphan Department",
            )

        self.assertIn(
            DEP_ORPHANED_DEPARTMENT_ERROR,
            cm.exception.messages,
        )

    def test_department_cannot_be_orphaned(self):

        company = self.create_company(
            name="ACME Ltd",
        )

        finance_department = self.create_department(
            name="Finance",
            company=company,
        )

        accounts_department = self.create_department(
            name="Accounts",
            parent=finance_department,
        )

        original = Department.objects.get(pk=accounts_department.pk)
        edited = Department.objects.get(pk=accounts_department.pk)
        edited.parent_department = None
        edited.company = None

        with self.assertRaises(ValidationError) as cm:
            DepartmentHierarchyService.apply_update(
                original=original,
                edited=edited,
            )

        self.assertIn(
            DEP_ORPHANED_DEPARTMENT_ERROR,
            cm.exception.messages,
        )