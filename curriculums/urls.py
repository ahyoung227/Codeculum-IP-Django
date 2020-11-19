from django.urls import path
from . import views

app_name = "curriculums"

urlpatterns = [
    path("<int:pk>", views.curriculum_detail, name="detail"),
    path("<int:pk>/edit/", views.EditCurriculumView.as_view(), name="edit"),
    path("search", views.SearchView.as_view(), name="search"),
    path("create/", views.CreateCurriculumView.as_view(), name="create"),
]
