from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    # Path Converters
    # int: numbers
    # str: strings
    # path: whole url
    # slug: hypen-underscore_stuff
    # UUID: universally unique identifer
    path('', views.all_specials, name="specials"),
    path('add_special', views.add_special, name="add-special"),
    path('update_special/<special_id>',
         views.update_special, name="update-special"),
    path('delete_special/<special_id>',
         views.delete_special, name="delete-special"),
]


# Configure admin titles
admin.site.site_header = "Hero's Administration"
admin.site.site_title = "Hero's Administration"
admin.site.index_title = "Welcome to the Hero's Admin Area"
