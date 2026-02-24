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
        
        # Send Emails
        try:
            print(f"\n📧 DEBUG: Starting email process...")
            print(f"📧 Sending to Admin: tarunkumargenji@gmail.com")
            
            # 1. Email to YOU (Admin)
            send_mail(
                subject=f"🔥 New Portfolio Query from {name}",
                message=f"You have a new message from your portfolio:\n\nName: {name}\nEmail: {email}\n\nMessage:\n{message_content}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['tarunkumargenji@gmail.com'],
                fail_silently=False,
            )
            print(f"✅ Admin email sent successfully!")
            
            print(f"📧 Sending to Visitor: {email}")
            # 2. Email to the USER (Visitor)
            send_mail(
                subject="Thank you for reaching out - Tarun Kumar Genji",
                message=f"Hi {name},\n\nThank you for visiting my portfolio and reaching out! I have received your message and will get back to you as soon as possible.\n\nBest Regards,\nTarun Kumar Genji",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
                fail_silently=False,
            )
            print(f"✅ Visitor email sent successfully!")
            
        except Exception as e:
            print("\n" + "❌"*25)
            print(f"📧 EMAIL SENDING FAILED!")
            print(f"Error Message: {str(e)}")
            print("❌"*25 + "\n")
            pass
            
        from accounts_app.models import Profile
        profile = Profile.objects.first()
        
        messages.success(request, f"Success! Emails have been sent to you and to {email}.")
        
        # WhatsApp Redirect (COMMENTED OUT TEMPORARILY FOR TESTING)
        # if profile and profile.phone_number:
        #     whatsapp_msg = f"Hi, I'm {name}. {message_content}"
        #     whatsapp_url = f"https://wa.me/{profile.phone_number}?text={whatsapp_msg.replace(' ', '%20')}"
        #     return redirect(whatsapp_url)
            
        return render(request, 'contact/contact.html')
            
        return redirect('contact')
        
    return render(request, 'contact/contact.html')
