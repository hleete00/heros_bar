from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from .models import Event
import json

# Create your tests here.


class EventTestViews(TestCase):

    def setUp(self):
        admin = User.objects.create_superuser(
            'admin', 'admin@admin.com', 'admin')
        self.client = Client()
        self.client.login(username=admin.username, password='admin')

        self.list_url = reverse('list-events')
        self.add_url = reverse('add-event')

    def test_event_list(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'events/event_list.html')

    def test_event_add(self):
        response = self.client.post(self.add_url, {
            'name': 'testName',
            'event_date': '2022-12-25',
            'event_time': '05:00',
            'genre': 'testGenre',
            'description': 'testDescription',

        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Event.objects.filter(
            pk=1).first().name, "testName")

    def test_event_update(self):
        Event.objects.create(
            name="testName", event_date="2022-12-25", event_time="05:00", genre="testGenre", description="testDescription")
        response = self.client.post(reverse('update-event', kwargs={'event_id': 1}), {
            'name': 'testNameUpdate',
            'event_date': '2022-12-25',
            'event_time': '05:00',
            'genre': 'testGenre',
            'description': 'testDescription',

        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Event.objects.filter(
            pk=1).first().name, "testNameUpdate")

    def test_event_delete(self):
        Event.objects.create(
            name="testName", event_date="2022-12-25", event_time="05:00", genre="testGenre", description="testDescription")
        response = self.client.post(
            reverse('delete-event', kwargs={'event_id': 1}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Event.objects.all().count(), 0)
