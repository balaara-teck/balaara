# models.py
from django.db import models

class ContactMessage(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.email}"

    class Meta:
        ordering = ['-submitted_at']
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"