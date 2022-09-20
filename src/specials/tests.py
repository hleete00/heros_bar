from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from .models import Specials
import json

# Create your tests here.


class SpecialTestViews(TestCase):

    def setUp(self):
        admin = User.objects.create_superuser(
            'admin', 'admin@admin.com', 'admin')
        self.client = Client()
        self.client.login(username=admin.username, password='admin')

        self.list_url = reverse('specials')
        self.add_url = reverse('add-special')

    def test_special_list(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'specials/specials.html')

    def test_special_add(self):
        response = self.client.post(self.add_url, {
            'special_text': 'testSpecial',
            'day': '1',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Specials.objects.filter(
            pk=1).first().special_text, "testSpecial")

    def test_special_update(self):
        Specials.objects.create(special_text="testSpecial", day="1")
        response = self.client.post(reverse('update-special', kwargs={'special_id': 1}), {
            'special_text': 'testSpecialUpdate',
            'day': '1',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Specials.objects.filter(
            pk=1).first().special_text, "testSpecialUpdate")

    def test_special_delete(self):
        Specials.objects.create(special_text="testSpecial", day="1")
        response = self.client.post(
            reverse('delete-special', kwargs={'special_id': 1}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Specials.objects.all().count(), 0)
