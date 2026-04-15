

from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from .forms import ContactMessageForm


def home(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # 1. Email sent to you (site owner)
            subject_owner = f"New Portfolio Message from {full_name}"
            message_owner = f"""
            You have received a new message from your portfolio website.

            Sender Name: {full_name}
            Sender Email: {email}

            Sender Message:
            {message}
            """
            
            send_mail(
                subject_owner,
                message_owner,
                settings.DEFAULT_FROM_EMAIL,
                ['balaarasolomon9@gmail.com'],
                fail_silently=False,
            )

            # 2. Confirmation email sent to the visitor
            subject_visitor = "Thank You for Contacting Balaara Solomon Ankyelle"
            message_visitor = f"""
            Dear {full_name},
            I have received your message and will get back to you as soon as possible.

            Here is a copy of your message:
            -----------------------------------
            {message}
            -----------------------------------

            Best regards,
            Balaara Solomon Ankyelle
            Mathematics & ICT Educator | Full-Stack Developer
            Email: balaarasolomon9@gmail.com
            GitHub: https://github.com/balaara-teck
            LinkedIn: https://www.linkedin.com/in/solomon-balaara-b94002291/
            """
            send_mail(
                subject_visitor,
                message_visitor,
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )

            messages.success(request, "Thank you! Your message has been sent successfully!")
            return redirect('home')
    else:
        form = ContactMessageForm()

    return render(request, 'home.html', {'form': form})

def profile(request):
    return render(request, 'profile.html')

