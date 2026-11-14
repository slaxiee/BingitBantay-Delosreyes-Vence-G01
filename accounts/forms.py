from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=150, required=True)
    last_name = forms.CharField(max_length=150, required=True)
    contact_number = forms.CharField(max_length=20, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'contact_number', 'role']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
            if name == 'contact_number':
                field.error_messages = {'required': 'Contact number cannot be left blank.'}


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'contact_number']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
            field.required = True
            field.error_messages = {
                'required': f'{field.label} cannot be left blank.'
            }