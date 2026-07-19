from django.contrib import admin

from .models import Organization


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