from django import forms
from home.models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ( 'name','surname','email','phone','message',)