from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from urllib3 import request
from .forms import ContactMessageForm

def profile(request):
    return render(request, 'profile.html')


def home(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you! Your message has been received successfully. I will get back to you as soon as possible.  Have a great day!   ")
            return redirect('home')  # Replace 'home' with your URL name
    else:
        form = ContactMessageForm()

    return render(request, 'home.html', {'form': form})
   