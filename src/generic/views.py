from django.shortcuts import render
from . import utils


def home(request):
    utils.contact(request)
    return render(request, 'generic/home.html')
