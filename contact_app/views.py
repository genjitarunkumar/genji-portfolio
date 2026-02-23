from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactMessage

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message_content = request.POST.get('message')
        
        # Save to DB
        ContactMessage.objects.create(name=name, email=email, message=message_content)
        
        # Send Email to Admin
        try:
            send_mail(
                subject=f"New Portfolio Message from {name}",
                message=f"From: {name} <{email}>\n\n{message_content}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER], # Admin email
                fail_silently=True,
            )
            
            # Send Confirmation to User
            send_mail(
                subject="Thank you for contacting me!",
                message=f"Hi {name},\n\nI have received your message and will get back to you soon.\n\nBest regards,\nPortfolio Admin",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
                fail_silently=True,
            )
        except:
            pass
            
        messages.success(request, "Your message has been sent successfully!")
        return redirect('contact')
        
    return render(request, 'contact/contact.html')
