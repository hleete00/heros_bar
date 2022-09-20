from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    # Path Converters
    # iint: numbers
    # str: strings
    # path: whole url
    # slug: hypen-underscore_stuff
    # UUID: universally unique identifer

    path('', views.all_events, name="list-events"),
    path('add_event', views.add_event, name="add-event"),
    path('update_event/<event_id>', views.update_event, name="update-event"),
    path('delete_event/<event_id>', views.delete_event, name="delete-event"),
]


# Configure admin titles
admin.site.site_header = "Hero's Administration"
admin.site.site_title = "Hero's Administration"
admin.site.index_title = "Welcome to the Hero's Admin Area"
