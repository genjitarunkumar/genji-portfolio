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
    
    profile = Profile.objects.get(user=request.user)
    projects_count = Project.objects.filter().count()
    
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
            
    return render(request, 'accounts/dashboard.html', {
        'profile': profile,
        'projects_count': projects_count
    })
