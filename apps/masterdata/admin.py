from django.contrib import admin

from .models import (
    Organization, 
    Party, 
    Person, 
    BusinessRelationship, 
    BusinessRelationshipParticipant,
    BusinessProcess,
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
    list_display = (
        "code",
        "name",
        "parent_process",
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
