from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from .models import Employee
import json

# Create your tests here.


class EmployeeTestCase(TestCase):

    def setUp(self):
        new_employee = Employee(
            name="unitTest", role="testEmployee", description="testDescription")
        new_employee.save()

    def test_employee_exists(self):
        employee_count = Employee.objects.all().count()
        self.assertEqual(employee_count, 1)
        self.assertNotEqual(employee_count, 0)

    def test_employee_name(self):
        employee = Employee.objects.filter(pk=1).first()
        self.assertEqual(employee.name, "unitTest")

    def test_employee_role(self):
        employee = Employee.objects.filter(pk=1).first()
        self.assertEqual(employee.role, "testEmployee")

    def test_employee_description(self):
        employee = Employee.objects.filter(pk=1).first()
        self.assertEqual(employee.description, "testDescription")

    def test_employee_delete(self):
        employee = Employee.objects.filter(pk=1)
        employee.delete()
        self.assertEqual(Employee.objects.all().count(), 0)
        self.assertNotEqual(Employee.objects.all().count(), 1)


class EmployeeTestViews(TestCase):

    def setUp(self):
        admin = User.objects.create_superuser(
            'admin', 'admin@admin.com', 'admin')
        self.client = Client()
        self.client.login(username=admin.username, password='admin')

        self.list_url = reverse('about-us')
        self.add_url = reverse('add-employee')

    def test_employee_list(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'about/about_us.html')

    def test_employee_add(self):
        response = self.client.post(self.add_url, {
            'name': 'testName',
            'role': 'testRole',
            'description': 'testDescription',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Employee.objects.filter(
            pk=1).first().name, "testName")

    def test_employee_update(self):
        Employee.objects.create(
            name="testName", role="testRole", description="testDescription")
        response = self.client.post(reverse('update-employee', kwargs={'employee_id': 1}), {
            'name': 'testNameUpdate',
            'role': 'testRole',
            'description': 'testDescription',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Employee.objects.filter(
            pk=1).first().name, "testNameUpdate")

    def test_employee_delete(self):
        Employee.objects.create(
            name="testName", role="testRole", description="testDescription")
        response = self.client.post(
            reverse('delete-employee', kwargs={'employee_id': 1}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Employee.objects.all().count(), 0)
