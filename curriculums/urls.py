from django.urls import path
from . import views

app_name = "curriculums"

urlpatterns = [path("<int:pk>", views.curriculum_detail, name="detail")]