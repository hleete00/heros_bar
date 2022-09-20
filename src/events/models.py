from django.db import models
from django.contrib.auth.models import User


class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=120)
    address = models.CharField(max_length=300)
    zip_code = models.CharField(max_length=10)
    phone = models.CharField('Contact Phone', max_length=25, blank=True)
    web = models.URLField('Website Address', blank=True)
    email = models.EmailField('Email', blank=True)

    def __str__(self):
        return self.name


class HerosUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField('User Email')

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Event(models.Model):
    name = models.CharField('Event Name', max_length=120)
    event_date = models.DateField()
    event_time = models.TimeField()
    genre = models.CharField(max_length=60)
    description = models.TextField(blank=True)
    photo = models.ImageField(
        upload_to='event_photos/', null=True, blank=True)

    def __str__(self):
        return self.name
