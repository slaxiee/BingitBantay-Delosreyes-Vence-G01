from django.contrib import admin
from .models import Complaint


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('id', 'resident', 'noise_type', 'severity', 'location', 'status', 'incident_time')
    list_filter = ('status', 'severity', 'noise_type')
    search_fields = ('location', 'description', 'resident__username')