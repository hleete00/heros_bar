from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField('Employee Name', max_length=120)
    role = models.CharField(max_length=60)
    description = models.TextField(blank=True)
    photo = models.ImageField(
        upload_to='employee_photos/', null=True, blank=True)
