from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
from django.utils.safestring import mark_safe

# Register your models here.


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        (
            "userAdmin",
            {
                "fields": (
                    "bio",
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
        "avatar_display",
    )

    def avatar_display(self, user):
        if user.avatar:
            return mark_safe(f'<img src="{user.avatar.url}"/>') 
        return None
