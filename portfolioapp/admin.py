# admin.py
from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'submitted_at')
    search_fields = ('full_name', 'email', 'message')
    list_filter = ('submitted_at',)
    readonly_fields = ('submitted_at',)