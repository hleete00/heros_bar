from django import forms
from django.forms import ModelForm
from .models import Employee


# create an event form
class EmployeeForm(ModelForm):

    # venue = forms.ModelChoiceField(queryset=Venue.objects.all(
    # ), widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Name of Venue'}))
    # manager = forms.ModelChoiceField(queryset=User.objects.all(
    # ), widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Manager of Event'}))

    class Meta:
        model = Employee
        fields = ('name', 'role', 'description', 'photo',)

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
            'name': forms.TextInput(attrs={'class': 'form-control bg-dark text-white', 'placeholder': 'Employee Name'}),
            'role': forms.TextInput(attrs={'class': 'form-control bg-dark text-white', 'placeholder': 'Role'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control bg-dark text-white'}),
            'description': forms.Textarea(attrs={'class': 'form-control bg-dark text-white', 'placeholder': 'Description'}),
        }
