from django.urls import path
from .views import home_view, about_view, projects_list, project_detail, resume_view

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('resume/', resume_view, name='resume'),
    path('projects/', projects_list, name='projects_list'),
    path('projects/<slug:slug>/', project_detail, name='project_detail'),
]
