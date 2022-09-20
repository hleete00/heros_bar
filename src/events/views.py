from django.shortcuts import render, redirect
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Event
from .forms import EventForm
from .utils import Calendar
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from generic import utils


@login_required
def add_event(request):
    utils.contact(request)
    submitted = False

    if request.method == "POST" and "eventButton" in request.POST:
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('add_event?submitted=True')
    else:
        form = EventForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'events/add_event.html', {"form": form, "submitted": submitted})


@login_required
def update_event(request, event_id):
    utils.contact(request)
    event = Event.objects.get(pk=event_id)
    form = EventForm(None, None, instance=event)

    if 'eventButton' in request.POST:
        form = EventForm(request.POST or None,
                         request.FILES or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('list-events')

    return render(request, 'events/update_event.html', {'event': event, 'form': form})


@login_required
def delete_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    if request.user.is_superuser:
        event.delete()
        messages.success(request, ("Event: " + event.name +
                         " on " + event.event_date.strftime("%B %d, %Y") + " deleted."))
        return redirect('list-events')
    else:
        messages.success(request, ("You are not authorized to delete events."))
        return redirect('list-events')


def all_events(request):
    utils.contact(request)
    event_list = Event.objects.filter(
        event_date__gte=datetime.now()).order_by('event_date')

    p = Paginator(Event.objects.filter(
        event_date__gte=datetime.now()).order_by('event_date'), 1)
    page = request.GET.get('page')
    events = p.get_page(page)
    nums = 'a' * events.paginator.num_pages

    cal = Calendar(datetime.now().year, datetime.now().month)
    html_cal = cal.format_month(withyear=True)

    return render(request, 'events/event_list.html', {'calendar': html_cal, 'event_list': event_list, 'events': events, 'nums': nums, })
