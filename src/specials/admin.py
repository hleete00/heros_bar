from django.contrib import admin
from .models import Specials
# Register your models here.


@admin.register(Specials)
class SpeicalAdmin(admin.ModelAdmin):
    list_display = ('special_text', 'day', )
    ordering = ('day',)
