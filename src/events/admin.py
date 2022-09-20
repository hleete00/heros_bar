from django.contrib import admin
from .models import Event, Venue, HerosUser

# Register your models here.
# admin.site.register(Event)
# admin.site.register(Venue)
admin.site.register(HerosUser)


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone')
    ordering = ('name',)
    search_fields = ('name', 'address')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = (('name',), 'event_date',
              'genre', 'description', 'photo')
    list_display = ('name', 'event_date')
    list_filter = ('event_date',)
    ordering = ('-event_date',)
