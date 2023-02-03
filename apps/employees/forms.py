from django import forms
from django.forms import ModelForm

from .models import (
    Employee
)


class EmployeeForm(ModelForm):
    prefix = "Employee"

    class Meta:
        model = Employee
        fields = "__all__"