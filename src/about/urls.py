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
    path('', views.about_us, name="about-us"),
    path('add_employee', views.add_employee, name="add-employee"),
    path('update_employee/<employee_id>',
         views.update_employee, name="update-employee"),
    path('delete_employee/<employee_id>',
         views.delete_employee, name="delete-employee"),
]


# Configure admin titles
admin.site.site_header = "Hero's Administration"
admin.site.site_title = "Hero's Administration"
admin.site.index_title = "Welcome to the Hero's Admin Area"
