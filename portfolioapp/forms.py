# forms.py
from django import forms
from .models import ContactMessage

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['full_name', 'email', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'placeholder': 'Your Name',
                'class': 'w-full bg-gray-100 border-none rounded-xl py-4 px-6 text-black focus:ring-2 focus:ring-blue-500 transition'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'email@example.com',
                'class': 'w-full bg-gray-100 border-none rounded-xl py-4 px-6 text-black focus:ring-2 focus:ring-blue-500 transition'
            }),
            'message': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'How can I help you?',
                'class': 'w-full bg-gray-100 border-none rounded-xl py-4 px-6 text-black focus:ring-2 focus:ring-blue-500 transition'
            }),
        }
        labels = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'message': 'Message',
        }