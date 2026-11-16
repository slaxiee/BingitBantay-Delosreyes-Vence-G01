from django import forms
from django.utils import timezone
from .models import Complaint


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['location', 'incident_time', 'noise_type', 'severity', 'description']
        widgets = {
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Purok 3, Sitio Sambag, near Barangay Chapel'
            }),
            'incident_time': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }),
            'noise_type': forms.Select(attrs={'class': 'form-select'}),
            'severity': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Describe the noise disturbance, estimated duration, and any landmarks...'
            }),
        }

    def clean_incident_time(self):
        incident_time = self.cleaned_data.get('incident_time')
        if incident_time and incident_time > timezone.now():
            raise forms.ValidationError("Incident date and time cannot be in the future.")
        return incident_time

    def clean_description(self):
        description = self.cleaned_data.get('description', '').strip()
        if len(description) < 10:
            raise forms.ValidationError("Please provide at least 10 characters describing the disturbance.")
        return description


class ComplaintReviewForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['status', 'staff_remarks']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-select'}),
            'staff_remarks': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter patrol response, warning issued, or resolution notes...'
            }),
        }
