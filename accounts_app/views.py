from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user, name=user.username)
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def dashboard_view(request):
    from django.core.mail import send_mail
    from django.conf import settings
    from projects_app.models import Project
    
    profile, created = Profile.objects.get_or_create(user=request.user, defaults={'name': request.user.username})
    projects = Project.objects.all().order_by('-created_date')
    projects_count = projects.count()
    
    if request.method == 'POST' and 'send_manual_email' in request.POST:
        target_email = request.POST.get('target_email')
        custom_message = request.POST.get('custom_message')
        subject = request.POST.get('subject', 'Message from Tarun Kumar')
        
        try:
            send_mail(
                subject=subject,
                message=custom_message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[target_email],
                fail_silently=False,
            )
            messages.success(request, f"Email sent successfully to {target_email}!")
        except Exception as e:
            messages.error(request, f"Failed to send email: {str(e)}")
            
    elif request.method == 'POST' and 'add_project' in request.POST:
        title = request.POST.get('title')
        description = request.POST.get('description')
        tech_stack = request.POST.get('tech_stack')
        github_link = request.POST.get('github_link', '')
        live_demo = request.POST.get('live_demo', '')
        
        try:
            Project.objects.create(
                title=title,
                description=description,
                tech_stack=tech_stack,
                github_link=github_link,
                live_demo=live_demo
            )
            messages.success(request, f"Project '{title}' added successfully!")
            return redirect('home')
        except Exception as e:
            messages.error(request, f"Failed to add project: {str(e)}")
            
    elif request.method == 'POST' and 'delete_project' in request.POST:
        project_id = request.POST.get('project_id')
        try:
            project = Project.objects.get(id=project_id)
            project_title = project.title
            project.delete()
            messages.success(request, f"Project '{project_title}' deleted successfully!")
            return redirect('dashboard')
        except Project.DoesNotExist:
            messages.error(request, "Project not found.")
        except Exception as e:
            messages.error(request, f"Failed to delete project: {str(e)}")
            
    elif request.method == 'POST' and 'edit_project' in request.POST:
        project_id = request.POST.get('project_id')
        try:
            project = Project.objects.get(id=project_id)
            project.title = request.POST.get('title')
            project.description = request.POST.get('description')
            project.tech_stack = request.POST.get('tech_stack')
            project.github_link = request.POST.get('github_link', '')
            project.live_demo = request.POST.get('live_demo', '')
            project.save()
            messages.success(request, f"Project '{project.title}' updated successfully!")
            return redirect('home')
        except Project.DoesNotExist:
            messages.error(request, "Project not found.")
        except Exception as e:
            messages.error(request, f"Failed to update project: {str(e)}")

    return render(request, 'accounts/dashboard.html', {
        'profile': profile,
        'projects': projects,
        'projects_count': projects_count
    })
