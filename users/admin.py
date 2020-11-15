from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    pass
    fieldsets = UserAdmin.fieldsets + (
        (
            "userAdmin",
            {
                "fields": (
                    "avatar",
                    "my_curriculums",
                    "subscribed_curriculum",
                    "saved_curriculum_titles",
                )
            },
        ),
    )
    list_filter = UserAdmin.list_filter + ("email",)

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "avatar",
    )
