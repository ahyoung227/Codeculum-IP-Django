from django.urls import path
from curriculums import views as curriculum_views

app_name = "core"

urlpatterns = [path("", curriculum_views.all_curriculums, name="curriculum")]