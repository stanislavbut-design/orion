from django.contrib import admin
from django import forms  

from .models import (
    Organization, 
    Party, 
    Person, 
    Product,
    Asset,
    Project,
    Department,
    ResponsibilityCenter,
    RoleType,
    BusinessRelationship, 
    BusinessRelationshipParticipant,
    BusinessProcess, 
)

from .services.department_hierarchy_service import (
    DepartmentHierarchyService,
)

class BusinessProcessAdminForm(forms.ModelForm):
    class Meta:
        model = BusinessProcess
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["parent_process"].label_from_instance = (
            lambda obj: f"{obj.code} — {obj.name}"
        )

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "public_id",
    )

    search_fields = (
        "name",
    )

    readonly_fields = (
        "public_id",
    )

    ordering = (
        "name",
    )

    def has_add_permission(self, request):
        return not Organization.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False
    
@admin.register(Party)
class PartyAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "legal_name",
        "party_type",
        "person",
        "party_code",
        "business_id",
    )

    list_filter = (
        "party_type",
        "person",
    )

    search_fields = (
        "name",
        "legal_name",
        "person__full_name",
        "business_id",
    )

    readonly_fields = (
        "public_id",
    )   

    ordering = (
        "name",
    )

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "short_name",
        "personal_id",
    )

    search_fields = (
        "full_name",
        "short_name",
        "personal_id",
    )

    readonly_fields = (
        "full_name",
        "short_name",
        "public_id",
    ) 

    ordering = (
        "last_name",
        "first_name",
        "middle_name",
    )

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "product_code",
        "name",
        "is_active",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "product_code",
        "name",
    )

    ordering = (
        "product_code",
        "name",
    )

    readonly_fields = (
        "id",
        "public_id",
        "created_at",
        "updated_at",
    )
@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = (
        "asset_code",
        "name",
        "reference",
        "is_active",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "asset_code",
        "name",
        "reference",
    )

    ordering = (
        "asset_code",
        "name",
    )

    readonly_fields = (
        "id",
        "public_id",
        "created_at",
        "updated_at",
    )

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "project_code",
        "name",
        "is_active",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "project_code",
        "name",
    )

    ordering = (
        "project_code",
        "name",
    )

    readonly_fields = (
        "id",
        "public_id",
        "created_at",
        "updated_at",
    )

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = (
        "department_code",
        "name",
        "company",
        "parent_department",
        "root_department",
        "responsibility_center",
        "is_active",
    )

    list_filter = (
        "root_department",
        "company",
        "responsibility_center",
        "is_active",        
    )

    search_fields = (
        "department_code",
        "name",
    )

    ordering = (
        "department_code",
        "name",
    )

    readonly_fields = (
        "id",
        "public_id",
        "created_at",
        "updated_at",
        "root_department",
    )

    list_select_related = (
        "company",
        "parent_department",
        "root_department",
        "responsibility_center",
    )


    def save_model(self, request, obj, form, change):

        if not change:

            DepartmentHierarchyService.initialize(obj)
            return

        original = Department.objects.get(pk=obj.pk)

        DepartmentHierarchyService.apply_update(
            original,
            obj,
        )

    def get_fields(self, request, obj=None):
        fields = [
            "department_code",
            "name",
            "description",
            "parent_department",
        ]

        if obj is None or obj.parent_department is None:
            fields.extend([
                "company",
                "responsibility_center",
            ])

        fields.extend([
            "root_department",
            "is_active",
            "id",
            "public_id",
            "created_at",
            "updated_at",
        ])

        return fields

@admin.register(ResponsibilityCenter)
class ResponsibilityCenterAdmin(admin.ModelAdmin):
    list_display = (
        "responsibility_center_code",
        "name",
        "parent_responsibility_center",
        "is_active",
    )

    list_filter = (
        "parent_responsibility_center",
        "is_active",        
    )

    search_fields = (
        "responsibility_center_code",
        "name",
    )

    ordering = (
        "responsibility_center_code",
        "name",
    )

    readonly_fields = (
        "id",
        "public_id",
        "created_at",
        "updated_at",
    )

@admin.register(RoleType)
class RoleTypeAdmin(admin.ModelAdmin):
    list_display = (
        "code",
        "name",
        "is_active",
        "sort_order",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "code",
        "name",
    )

    ordering = (
        "sort_order",
        "name",
    )

@admin.register(BusinessRelationship)
class BusinessRelationshipAdmin(admin.ModelAdmin):
    list_display = (
        "relationship_type",
        "effective_from",
        "effective_to",
    )

    list_filter = (
        "relationship_type",
    )

    readonly_fields = (
        "public_id",
    )

    search_fields = (
        "relationship_type",
    )

    ordering = (
        "relationship_type",
        "effective_from",
    )


@admin.register(BusinessRelationshipParticipant)
class BusinessRelationshipParticipantAdmin(admin.ModelAdmin):
    list_display = (
        "business_relationship",
        "role_type",
        "party",
        "person",
    )

    list_filter = (
        "role_type",
    )

    readonly_fields = (
        "public_id",
    )

    search_fields = (
        "role_type",
    )

@admin.register(BusinessProcess)
class BusinessProcessAdmin(admin.ModelAdmin):

    form = BusinessProcessAdminForm
    
    list_display = (
        "code",
        "name",
        "parent_code",
    )

    readonly_fields = (
        "public_id",
    )

    search_fields = (
        "code",
        "name",
    )

    ordering = (
        "code",
    )

    @admin.display(
        description="Parent",
        ordering="parent_process__code",
    )
    def parent_code(self, obj):
        if obj.parent_process:
            return obj.parent_process.code
        return ""

