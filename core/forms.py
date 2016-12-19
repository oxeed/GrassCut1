from django import forms
from django.forms import Textarea, TextInput
from .models import Client
from django.utils.translation import ugettext_lazy as _


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['full_name', 'email', 'tel_number', 'note']
        labels = {
            'full_name': _(''),   # delete labels from forms
            'email': _(''),
            'tel_number': _(''),
            'note': _('')
        }

        widgets = {
            'full_name': TextInput(attrs={'placeholder': 'Vārds Uzvārds'}),
            'email': TextInput(attrs={'placeholder': 'E-pasts'}),
            'tel_number': TextInput(attrs={'placeholder': 'Telefona numurs'}),
            'note': Textarea(attrs={'placeholder': 'Piezīmes'}),

        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, provider = email.split('@')
        domain, extension = provider.split('.')

        return email

    def clean_tel_number(self):
        tel_number = self.cleaned_data.get('tel_number')
        return tel_number

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        return full_name
