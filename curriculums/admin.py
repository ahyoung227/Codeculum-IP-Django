from django.contrib import admin
from . import models


@admin.register(models.Skill)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin definition"""

    pass


@admin.register(models.Curriculum)
class CurriculumAdmin(admin.ModelAdmin):

    """ Curriculum Admin definition"""

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("title", "description", "created_date")},
        ),
        (
            "Other Info",
            {
                "fields": (
                    "budget",
                    "period",
                    "education_background",
                    "related_skill",
                    "owner",
                )
            },
        ),
    )

    list_display = (
        "title",
        "created_date",
        "period",
        "budget",
        "education_background",
        "owner",
    )

    ordering = ("title", "budget")

    list_filter = (
        "period",
        "budget",
    )

    search_fields = ("period", "budget")

    filter_horizontal = ("related_skill",)

    raw_id_fields = ("owner",)


@admin.register(models.Day)
class TaskAdmin(admin.ModelAdmin):

    pass


@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):

    pass