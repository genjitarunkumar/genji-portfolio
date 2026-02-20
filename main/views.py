from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import Profile, Skill, Project, ContactMessage

def home(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    # Show top 3 projects
    projects_list = Project.objects.all().order_by('-created_date')[:3]
    
    success = False
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )

        # Send message directly to the user
        try:
            send_mail(
                subject=f"Message from Tarun Kumar Genji",
                message=f"Hi {name},\n\nYou have a new message:\n\n{message}\n\nBest regards,\nTarun Kumar Genji",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],
                fail_silently=False,
            )
            # Send notification to you (the Admin)
            send_mail(
                subject=f"📬 New Contact Message from {name}",
                message=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
        except Exception as e:
            print(f"Error sending email in home view: {e}")
            pass
            
        success = True

    return render(request, 'home.html', {
        'profile': profile, 
        'skills': skills, 
        'projects': projects_list,
        'success': success
    })

def projects(request):
    projects_list = Project.objects.all().order_by('-created_date')
    return render(request, 'projects.html', {'projects': projects_list})

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'project_detail.html', {'project': project})

def contact(request):
    success = False
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )

        # Send message directly to the user
        try:
            send_mail(
                subject=f"Message from Tarun Kumar Genji",
                message=f"Hi {name},\n\nYou have a new message:\n\n{message}\n\nBest regards,\nTarun Kumar Genji",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],
                fail_silently=False,
            )
            # Send notification to you (the Admin)
            send_mail(
                subject=f"📬 New Contact Message from {name}",
                message=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
        except Exception as e:
            print(f"Email error: {e}")
            pass
        success = True
        
    return render(request, 'contact.html', {'success': success})
