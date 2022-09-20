from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Specials
from .forms import SpecialForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from generic import utils


def all_specials(request):
    utils.contact(request)
    monday_specials = Specials.objects.filter(day=1)
    tuesday_specials = Specials.objects.filter(day=2)
    wednesday_specials = Specials.objects.filter(day=3)
    thursday_specials = Specials.objects.filter(day=4)
    friday_specials = Specials.objects.filter(day=5)
    saturday_specials = Specials.objects.filter(day=6)
    sunday_specials = Specials.objects.filter(day=7)

    return render(request, 'specials/specials_list.html', {'monday_specials': monday_specials,
                                                           'tuesday_specials': tuesday_specials,
                                                           'wednesday_specials': wednesday_specials,
                                                           'thursday_specials': thursday_specials,
                                                           'friday_specials': friday_specials,
                                                           'saturday_specials': saturday_specials,
                                                           'sunday_specials': sunday_specials, })


@login_required
def add_special(request):
    utils.contact(request)
    submitted = False
    if request.method == "POST":
        form = SpecialForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('add_special?submitted=True')
    else:
        form = SpecialForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'specials/add_special.html', {"form": form, "submitted": submitted})


@login_required
def update_special(request, special_id):
    utils.contact(request)
    special = Specials.objects.get(pk=special_id)
    form = SpecialForm(None, instance=special)

    if 'specialButton' in request.POST:
        form = SpecialForm(request.POST or None, instance=special)

    if special.day == '1':
        day = 'Monday'
    elif special.day == '2':
        day = 'Tuesday'
    elif special.day == '3':
        day = 'Wednesday'
    elif special.day == '4':
        day = 'Thursday'
    elif special.day == '5':
        day = 'Friday'
    elif special.day == '6':
        day = 'Saturday'
    elif special.day == '7':
        day = 'Sunday'

    if form.is_valid():
        form.save()
        messages.success(request, ("Special: " + special.special_text +
                         " on " + day + " updated."))
        return redirect('specials')

    return render(request, 'specials/update_special.html', {'special': special, 'form': form})


@login_required
def delete_special(request, special_id):
    special = Specials.objects.get(pk=special_id)
    if special.day == '1':
        day = 'Monday'
    elif special.day == '2':
        day = 'Tuesday'
    elif special.day == '3':
        day = 'Wednesday'
    elif special.day == '4':
        day = 'Thursday'
    elif special.day == '5':
        day = 'Friday'
    elif special.day == '6':
        day = 'Saturday'
    elif special.day == '7':
        day = 'Sunday'
    if request.user.is_superuser:
        special.delete()
        messages.success(request, ("Special: " + special.special_text +
                         " on " + day + " deleted."))
        return redirect('specials')
    else:
        messages.success(
            request, ("You are not authorized to delete specials."))
        return redirect('specials')
