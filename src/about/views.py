from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Employee
from .forms import EmployeeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from generic import utils

# Create your views here.


def about_us(request):
    utils.contact(request)
    employees = Employee.objects.all()
    return render(request, 'about/about_us.html', {'employees': employees})


@login_required
def add_employee(request):
    utils.contact(request)
    submitted = False

    if request.method == "POST" and "employeeButton" in request.POST:
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('add_employee?submitted=True')
    else:
        form = EmployeeForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'about/add_employee.html', {"form": form, "submitted": submitted})


@login_required
def update_employee(request, employee_id):
    utils.contact(request)
    employee = Employee.objects.get(pk=employee_id)
    form = EmployeeForm(None, None, instance=employee)

    if "employeeButton" in request.POST:
        form = EmployeeForm(request.POST or None,
                            request.FILES or None, instance=employee)

    if form.is_valid():
        form.save()
        messages.success(request, ("Employee: " + employee.name + " updated."))
        return redirect('about-us')

    return render(request, 'about/update_employee.html', {'employee': employee, 'form': form})


@login_required
def delete_employee(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)

    if request.user.is_superuser:
        employee.delete()
        messages.success(request, ("Employee: " + employee.name + " deleted."))
        return redirect('about-us')
    else:
        messages.success(
            request, ("You are not authorized to delete employees."))
        return redirect('about-us')
