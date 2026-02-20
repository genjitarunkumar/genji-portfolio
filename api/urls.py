from django.urls import path
from .views import ProjectListAPI, ProjectDetailAPI, ProjectCreateAPI, ContactAPI

urlpatterns = [
    path('projects/', ProjectListAPI.as_view(), name='api-project-list'),
    path('projects/create/', ProjectCreateAPI.as_view(), name='api-project-create'),
    path('projects/<slug:slug>/', ProjectDetailAPI.as_view(), name='api-project-detail'),
    path('contact/', ContactAPI.as_view(), name='api-contact'),
]
