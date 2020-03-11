from django.shortcuts import render, HttpResponse, redirect, get_list_or_404, get_object_or_404
from .forms import EmployeeForm
from .models import *
# Create your views here.


def index(request):
    return render(request, "index.html")


def employee_list(request):
    content = {'employee_list': Employee.objects.all()}
    return render(request, "emp_list.html", content)


def employee_form(request):
    if request.method == "GET":
        form = EmployeeForm()
        return render(request, 'emp_form.html', {'form': form})
    else:
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('employee_list')


def employee_delete(request):
    employee = Employee.objects.get(pk.id)
    employee.delete()

    return redirect('employee_list')


def edit_items(request, pk, Employee, cls):
    item = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
    else:
        form = cls(instance=item)
        return render(request,)

    return render(request, 'empedit.html', {'form': form})


def edit_employee(request, pk):
    return edit_items(request, pk, Employee, EmployeeForm)
