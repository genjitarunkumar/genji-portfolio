from django.urls import path
from .views import projects_api

urlpatterns = [
    path('projects/', projects_api, name='projects_api'),
]
