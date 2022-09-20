from django.db import models

# Create your models here.


class Specials(models.Model):
    DAY_OF_THE_WEEK = (
        ('1', 'Monday'),
        ('2', 'Tuesday'),
        ('3', 'Wednesday'),
        ('4', 'Thursday'),
        ('5', 'Friday'),
        ('6', 'Saturday'),
        ('7', 'Sunday'),
    )
    special_text = models.CharField(max_length=200)
    day = models.CharField(max_length=50, choices=DAY_OF_THE_WEEK)
