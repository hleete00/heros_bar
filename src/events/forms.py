from django import forms
from django.forms import ModelForm
from .models import Event, Venue
from django.contrib.auth.models import User
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime


# create an event form
class EventForm(ModelForm):

    # venue = forms.ModelChoiceField(queryset=Venue.objects.all(
    # ), widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Name of Venue'}))
    # manager = forms.ModelChoiceField(queryset=User.objects.all(
    # ), widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Manager of Event'}))

    class Meta:
        model = Event
        fields = ('name', 'event_date', 'event_time',
                  'genre', 'photo', 'description')

        # labels = {
        #     'name': '',
        #     'event_date': '',
        #     'event_time': '',
        #     'venue': '',
        #     'manager': '',
        #     'genre': '',
        #     'description': '',
        # }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control bg-dark text-white', 'placeholder': 'Performance Name'}),
            'event_date': forms.widgets.DateInput(attrs={'type': 'date', 'class': 'form-control bg-dark text-white', 'placeholder': 'Date of Event'}),
            'event_time': forms.widgets.TimeInput(attrs={'type': 'time', 'class': 'form-control bg-dark text-white', 'placeholder': 'Time Event Starts'}),
            'genre': forms.TextInput(attrs={'class': 'form-control bg-dark text-white', 'placeholder': 'Genre'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control bg-dark text-white'}),
            'description': forms.Textarea(attrs={'class': 'form-control bg-dark text-white', 'placeholder': 'Description'}),
        }
