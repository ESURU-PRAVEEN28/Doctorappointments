
# forms.py
from django import forms
from .models import Doctor

class EmailForm(forms.Form):
    name = forms.CharField(max_length=100, label='Subject')
    recipient = forms.EmailField(label='Recipient Email')
    message = forms.CharField(max_length=100, label='Message')
    doctors=forms.fields_for_model('specialization',)


