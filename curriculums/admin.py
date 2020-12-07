from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(models.Skill)
class ItemAdmin(admin.ModelAdmin):
    """ Item Admin definition"""

    pass


class PhotoInline(admin.TabularInline):

    model = models.Photo


@admin.register(models.Curriculum)
class CurriculumAdmin(admin.ModelAdmin):

    """ Curriculum Admin definition"""

    inlines = (PhotoInline,)

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("title", "description", "learning_goal")},
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
        # "created_date",
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


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ Item Admin definition"""

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img src="{obj.file.url}" width="130px" height="100px"/>')

    get_thumbnail.short_description = "Thumbnail"


@admin.register(models.Day)
class DayAdmin(admin.ModelAdmin):
    """ Task Admin definition"""

    pass


@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    """ Task Admin definition"""

    pass
