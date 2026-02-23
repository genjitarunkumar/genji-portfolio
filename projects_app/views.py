from django.shortcuts import render, get_object_or_404, redirect
from .models import Project
from accounts_app.models import Profile

def home_view(request):
    profile = Profile.objects.first()
    projects = Project.objects.all()[:3]
    return render(request, 'home.html', {'profile': profile, 'projects': projects})

def about_view(request):
    profile = Profile.objects.first()
    return render(request, 'about.html', {'profile': profile})

def projects_list(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'project_detail.html', {'project': project})
