from django.urls import path
from .views import ProjectListAPI, ProjectDetailAPI

urlpatterns = [
    path('projects/', ProjectListAPI.as_view(), name='api-project-list'),
    path('projects/<slug:slug>/', ProjectDetailAPI.as_view(), name='api-project-detail'),
]
