from django import forms
from .models import Position, Employee


# class PositionFrom(forms.ModelForm):
#     class Meta:
#         model = Position
#         fields = ('title')


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('fullname', 'emp_code', 'phone_number', 'position')
