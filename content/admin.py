from admin_auto_filters.filters import AutocompleteFilterFactory
from django.contrib import admin
from django.contrib.admin.utils import model_ngettext
from django.utils.translation import gettext_lazy as _

from admin.models import ModelAdmin
from admin.utils.urls import admin_model_view_link
from content.models import Culture, Region, House, Character


@admin.register(Culture)
class CultureAdmin(ModelAdmin):
    search_fields = ["name"]
    readonly_fields = [
        "uuid",
        "created_at",
        "updated_at",
    ]

    list_display = [
        "name",
        "created_at",
    ]

    date_hierarchy = "created_at"
    ordering = ["name"]

    add_fieldsets = (
        (
            None,
            {
                "fields": [
                    "name",
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
                    "name",
                    "metadata",
                    "created_at",
                    "updated_at",
                ]
            },
        ),
    )

    class Media:
        pass


@admin.register(Region)
class RegionAdmin(ModelAdmin):
    search_fields = ["name"]
    readonly_fields = [
        "uuid",
        "num_houses",
        "num_houses_link",
        "created_at",
        "updated_at",
    ]

    list_display = [
        "name",
        "num_houses",
        "created_at",
    ]

    def num_houses(self, obj):
        return obj.num_houses

    num_houses.admin_order_field = "num_houses"
    num_houses.short_description = _("Houses")

    def num_houses_link(self, obj):
        if not obj.pk:
            return
        return admin_model_view_link(
            House,
            "changelist",
            f"{obj.num_houses} {model_ngettext(House, obj.num_houses)}",
            query_kwargs={"region": obj.pk},
        )

    num_houses_link.short_description = _("Houses")

    date_hierarchy = "created_at"
    ordering = ["name"]

    add_fieldsets = (
        (
            None,
            {
                "fields": [
                    "name",
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
                    "name",
                    "num_houses_link",
                    "metadata",
                    "created_at",
                    "updated_at",
                ]
            },
        ),
    )

    class Media:
        pass


@admin.register(House)
class HouseAdmin(ModelAdmin):
    search_fields = ["name"]
    readonly_fields = [
        "uuid",
        "created_at",
        "updated_at",
    ]
    autocomplete_fields = [
        "region",
        "lord",
        "heir",
        "overlord",
        "founder",
    ]

    list_display = [
        "name",
        "region",
        "founder",
        "lord",
        "heir",
        "overlord",
        "created_at",
    ]
    list_filter = [
        AutocompleteFilterFactory(_("Region"), "region"),
        AutocompleteFilterFactory(_("Founder"), "founder"),
        AutocompleteFilterFactory(_("Lord"), "lord"),
        AutocompleteFilterFactory(_("Heir"), "heir"),
        AutocompleteFilterFactory(_("Overlord"), "overlord"),
    ]

    date_hierarchy = "created_at"
    ordering = ["name"]

    add_fieldsets = (
        (
            None,
            {
                "fields": [
                    "name",
                    "region",
                    "coat_of_arms",
                    "words",
                    "founded",
                    "founder",
                    "lord",
                    "heir",
                    "overlord",
                    "seats",
                    "ancestral_weapons",
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
                    "name",
                    "region",
                    "coat_of_arms",
                    "words",
                    "founded",
                    "founder",
                    "lord",
                    "heir",
                    "overlord",
                    "seats",
                    "ancestral_weapons",
                    "metadata",
                    "created_at",
                    "updated_at",
                ]
            },
        ),
    )

    class Media:
        pass


@admin.register(Character)
class CharacterAdmin(ModelAdmin):
    search_fields = ["name"]
    readonly_fields = [
        "uuid",
        "created_at",
        "updated_at",
    ]
    autocomplete_fields = [
        "culture",
        "mother",
        "father",
        "spouse",
        "allegiances",
    ]

    list_display = [
        "name",
        "gender",
        "culture",
        "mother",
        "father",
        "spouse",
        "created_at",
    ]
    list_filter = [
        "gender",
        AutocompleteFilterFactory(_("Culture"), "culture"),
        AutocompleteFilterFactory(_("Mother"), "mother"),
        AutocompleteFilterFactory(_("Father"), "father"),
        AutocompleteFilterFactory(_("Spouse"), "spouse"),
    ]

    date_hierarchy = "created_at"
    ordering = ["name"]

    add_fieldsets = (
        (
            None,
            {
                "fields": [
                    "name",
                    "gender",
                    "culture",
                    "born",
                    "died",
                    "mother",
                    "father",
                    "spouse",
                    "allegiances",
                    "titles",
                    "aliases",
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
                    "name",
                    "gender",
                    "culture",
                    "born",
                    "died",
                    "mother",
                    "father",
                    "spouse",
                    "allegiances",
                    "titles",
                    "aliases",
                    "metadata",
                    "created_at",
                    "updated_at",
                ]
            },
        ),
    )

    class Media:
        pass
