from django.contrib import admin

from .models import Organization, Party, Person, BusinessRelationship


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
        "party_code",
        "business_id",
    )

    list_filter = (
        "party_type",
    )

    search_fields = (
        "name",
        "legal_name",
        "business_id",
    )

    readonly_fields = (
        "public_id",
    )

    exclude = (
        "organization",
    )   

    ordering = (
        "name",
    )

    def save_model(self, request, obj, form, change):
        if obj.organization_id is None:
            obj.organization = Organization.objects.get()

        super().save_model(request, obj, form, change)

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

    exclude = (
        "organization",
    )   

    ordering = (
        "last_name",
        "first_name",
        "middle_name",
    )

    def save_model(self, request, obj, form, change):
        if obj.organization_id is None:
            obj.organization = Organization.objects.get()

        super().save_model(request, obj, form, change)

@admin.register(BusinessRelationship)
class BusinessRelationshipAdmin(admin.ModelAdmin):
    list_display = (
        "relationship_type",
        "organization",
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