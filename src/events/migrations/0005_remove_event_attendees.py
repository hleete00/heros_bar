# Generated by Django 4.0.5 on 2022-07-07 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_remove_event_manager_remove_event_venue'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='attendees',
        ),
    ]