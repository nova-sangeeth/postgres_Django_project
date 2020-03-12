from django.shortcuts import render, HttpResponse, redirect, get_list_or_404, get_object_or_404
from .forms import EmployeeForm
from .models import *
# Create your views here.


def index(request):
    return render(request, "index.html")


def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, "employee_list.html", context)

# Try the inherited method like the inventory...


def employee_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "employee_form.html", {'form': form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
        return redirect('employee_list')


def employee_delete(request, id):
    employee = Employee.objects.get(pk=id).delete()
    # employee.delete()
    return redirect('employee_list')
