from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from access.models import User
from admin.mixins import OverridesMixin

admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(OverridesMixin, BaseUserAdmin):
    save_on_top = True
    add_form_template = "admin/change_form.html"

    autocomplete_fields = []
    search_fields = ["email", "name"]
    readonly_fields = ["uuid", "created_at", "updated_at"]

    list_display = [
        "email",
        "name",
        "is_active",
        "created_at",
    ]
    list_filter = ["is_active", "created_at"]
    filter_horizontal = []

    date_hierarchy = "created_at"
    ordering = ["-created_at"]

    add_fieldsets = (
        (
            None,
            {
                "fields": [
                    "email",
                    "name",
                    "is_active",
                    "password1",
                    "password2",
                    "metadata",
                ]
            },
        ),
    )

    fieldsets = (
        (
            None,
            {
                "fields": [
                    "uuid",
                    "email",
                    "name",
                    "is_active",
                    "password",
                    "metadata",
                    "created_at",
                    "updated_at",
                ]
            },
        ),
    )

    class Media:
        pass
