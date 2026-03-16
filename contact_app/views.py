from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactMessage

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        message_content = request.POST.get('message', '').strip()
        
        # 1. Save to Database
        ContactMessage.objects.create(name=name, email=email, message=message_content)
        
        print(f"\n--- NEW CONTACT FORM SUBMISSION ---")
        print(f"Name: {name}")
        print(f"Visitor Email: {email}")

        error_count = 0

        # 2. Email to Admin (YOU)
        try:
            send_mail(
                subject=f"🔥 New Portfolio Query: {name}",
                message=f"Hello Tarun,\n\nYou have a new message from your portfolio.\n\nSender: {name}\nSender Email: {email}\n\nMessage:\n{message_content}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            print(f"✅ Admin notification sent to {settings.EMAIL_HOST_USER}")
        except Exception as e:
            print(f"❌ Admin notification failed: {e}")
            error_count += 1

        # 3. Email to Visitor (THE USER)
        try:
            send_mail(
                subject="Thank you for contacting Tarun Kumar Genji",
                message=f"Hi {name},\n\nThank you for reaching out via my portfolio! I have received your message and will get back to you shortly.\n\nYour Message Reference:\n\"{message_content}\"\n\nBest Regards,\nTarun Kumar Genji",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],
                fail_silently=False,
            )
            print(f"✅ Visitor confirmation sent to {email}")
        except Exception as e:
            print(f"❌ Visitor confirmation failed for {email}: {e}")
            error_count += 1

        if error_count == 0:
            messages.success(request, f"Success! Your message has been sent. A confirmation email was sent to {email}.")
        elif error_count < 2:
            messages.warning(request, "Your message was saved, but we had trouble sending one of the emails.")
        else:
            messages.error(request, "We couldn't send the emails, but your message has been saved.")

        return redirect('contact')
    
    # Message for when they land on the page
    messages.info(request, "✨ Thanks for visiting us! Feel free to reach out using the form below.")
    return render(request, 'contact/contact.html')


