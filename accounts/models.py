from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('resident', 'Resident'),
        ('tanod', 'Barangay Tanod'),
        ('official', 'Barangay Official'),
    )
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='resident')
    is_approved = models.BooleanField(default=True)
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"