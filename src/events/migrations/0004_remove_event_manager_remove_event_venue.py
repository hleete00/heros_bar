# Generated by Django 4.0.5 on 2022-07-07 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_event_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='manager',
        ),
        migrations.RemoveField(
            model_name='event',
            name='venue',
        ),
    ]
