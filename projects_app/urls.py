from django.urls import path
from .views import home_view, about_view, projects_list, project_detail

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('projects/', projects_list, name='projects_list'),
    path('projects/<slug:slug>/', project_detail, name='project_detail'),
]
