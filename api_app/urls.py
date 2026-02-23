from django.urls import path
from .views import ProjectListAPI, ProjectDetailAPI, ContactCreateAPI

urlpatterns = [
    path('projects/', ProjectListAPI.as_view(), name='api_projects_list'),
    path('projects/<slug:slug>/', ProjectDetailAPI.as_view(), name='api_project_detail'),
    path('contact/', ContactCreateAPI.as_view(), name='api_contact_create'),
]
