from django import forms
from .models import contactform

class contact(forms.ModelForm):
    class Meta:
        model = contactform
        fields = ['name', 'email', "subject","phone","message"]
