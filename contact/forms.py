from django import forms
from .models import ContactModel


class ContactForm(forms.ModelForm):
    """Класс описания формы на странице контактов"""
    class Meta:
        model = ContactModel
        fields = '__all__'