from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
import json

# Create your tests here.


class MemberTestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.credentials = {
            'username': 'testUser',
            'password': 'testPassword',
        }
        User.objects.create_user(**self.credentials)

        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.register_url = reverse('register')

    def test_login_user(self):
        response = self.client.post(
            self.login_url, self.credentials, follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertTrue(response.context['user'].is_active)
        self.assertTemplateUsed(response, 'events/home.html')

    def test_logout_user(self):
        self.client.login(**self.credentials)
        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, 302)

    def test_user_register(self):
        response = self.client.post(self.register_url, {
            'username': 'testUsername',
            'first_name': 'testFirstName',
            'last_name': 'testLastName',
            'email': 'testEmail@email.com',
            'password1': 'testPassword',
            'password2': 'testPassword',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.filter(
            pk=2).first().username, "testUsername")
