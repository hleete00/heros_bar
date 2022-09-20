from django import forms
from django.forms import ModelForm
from .models import Specials
from django.contrib.auth.models import User


class SpecialForm(ModelForm):

    class Meta:
        model = Specials
        fields = ('special_text', 'day')

        widgets = {
            'special_text': forms.TextInput(attrs={'class': 'form-control bg-dark text-white', 'placeholder': 'Special Text'}),
            'day': forms.Select(attrs={'class': 'form-control bg-dark text-white'}),
        }
