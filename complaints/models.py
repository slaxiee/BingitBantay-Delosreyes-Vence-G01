from django.conf import settings
from django.db import models


class Complaint(models.Model):
    NOISE_TYPE_CHOICES = [
        ('videoke', 'Loud Videoke / Karaoke'),
        ('party', 'Loud Party / Gathering'),
        ('construction', 'After-Hours Construction'),
        ('vehicle', 'Modified Muffler / Vehicle Noise'),
        ('animal', 'Unattended Barking / Animal Noise'),
        ('other', 'Other Noise Disturbance'),
    ]

    SEVERITY_CHOICES = [
        ('low', 'Low - Minor Disturbance'),
        ('medium', 'Medium - Disruptive'),
        ('high', 'High - Severe / Sleep Disruption'),
    ]

    STATUS_CHOICES = [
        ('filed', 'Filed'),
        ('under_review', 'Under Review'),
        ('resolved', 'Resolved'),
    ]

    resident = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='complaints'
    )
    location = models.CharField(max_length=255)
    incident_time = models.DateTimeField()
    noise_type = models.CharField(max_length=30, choices=NOISE_TYPE_CHOICES)
    severity = models.CharField(max_length=15, choices=SEVERITY_CHOICES, default='medium')
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='filed')
    staff_remarks = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"#{self.id} - {self.get_noise_type_display()} at {self.location} ({self.get_status_display()})"