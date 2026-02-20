from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
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

        # Send email to yourself
        try:
            send_mail(
                subject=f"📬 New Contact Message from {name}",
                message=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['tarunkumargenji@gmail.com'],
                fail_silently=False,
            )
            
            # Send confirmation to user
            send_mail(
                subject="Thank you for contacting Tarun",
                message=f"Hi {name},\n\nI have received your message and will get back to you shortly.\n\nBest regards,\nTarun Kumar Genji",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],
                fail_silently=False,
            )
        except Exception:
            pass # Silent fail if email settings aren't configured
            
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

        # Send email to admin
        try:
            send_mail(
                subject=f"📬 New Contact Message from {name}",
                message=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
                from_email='tarunkumargenji@gmail.com',  # Your authenticated email
                recipient_list=['tarunkumargenji@gmail.com'],
                fail_silently=False,
            )
            
            # Send confirmation to user
            send_mail(
                subject="Thank you for contacting Tarun",
                message=f"Hi {name},\n\nI have received your message and will get back to you shortly.\n\nBest regards,\nTarun Kumar Genji",
                from_email='tarunkumargenji@gmail.com',
                recipient_list=[email],
                fail_silently=False,
            )
        except Exception as e:
            print(f"Email error: {e}")
            pass
        success = True
        
    return render(request, 'contact.html', {'success': success})
