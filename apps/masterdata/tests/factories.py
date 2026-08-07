from apps.masterdata.models import (
    Party,
    Department,
    ResponsibilityCenter,
)

from apps.masterdata.services.department_hierarchy_service import (
    DepartmentHierarchyService,
)


class MasterDataFactoryMixin:
    """
    Helper methods for creating Master Data objects.
    """

    def create_company(
        self,
        name="Company",
        party_type="LEGAL_ENTITY",
    ):
        return Party.objects.create(
            name=name,
            party_type=party_type,
        )

    def create_responsibility_center(
        self,
        name="RC",
        parent=None,
    ):
        return ResponsibilityCenter.objects.create(
            name=name,
            parent_responsibility_center=parent,
        )

    def create_department(
        self,
        name,
        parent=None,
        company=None,
        responsibility_center=None,
    ):
        department = Department(
            name=name,
            parent_department=parent,
            company=company,
            responsibility_center=responsibility_center,
        )

        DepartmentHierarchyService.initialize(department)

        return department