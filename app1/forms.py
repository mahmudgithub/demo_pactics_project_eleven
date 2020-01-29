from django import forms
from myapp.models import Contact

class ContactForm(forms.ModelForm):

    class Meta:
        model=Contact
        fields=['contact_name','contact_group','phone','email',]
        widgets = {
            'contact_name': forms.TextInput(attrs={'required': True}),
            'phone': forms.TextInput(attrs={'required': True}),
            'Email': forms.EmailInput(attrs={'required': True}),
        }