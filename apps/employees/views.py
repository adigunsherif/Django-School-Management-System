import csv

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.forms import widgets
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, View
from django.shortcuts import HttpResponseRedirect, redirect, render
from django.views.generic.edit import CreateView, DeleteView, UpdateView

#from apps.finance.models import Invoice

from .models import Employee, EmployeeBulkUpload

from .forms import (
    EmployeeForm
)



class EmployeeListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Employee
    # context_object_name = 'employee_list'   # your own name for the list as a template variable
    template_name = "employees/employee_list.html" # own template name/location

    """ def get_context_data(request):
        context = super().get_context_data(**kwargs)
        context["form"] = EmployeeForm()
        context ={}
        context["employees"] = Employee.objects.all()
        return context """

    def get_context_data(self, **kwargs):
        context = super(EmployeeListView, self).get_context_data(**kwargs)
        # context["employees"] = Employee.objects.filter(current_status='active') # Get 5 employees with status 'active'
        context["employees"] = Employee.objects.all()
        return context


class EmployeeDetailView(LoginRequiredMixin, DetailView):
    model = Employee
    template_name = "employees/employee_detail.html"

    def get_context_data(self, **kwargs):
        context = super(EmployeeDetailView, self).get_context_data(**kwargs)
    #    context["payments"] = Invoice.objects.filter(employee=self.object)
        return context


class EmployeeCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Employee
    fields = "__all__"
    success_message = "Новый сотрудник успешно добавлен."

    def get_form(self):
        """add date picker in forms"""
        form = super(EmployeeCreateView, self).get_form()
        form.fields["date_of_birth"].widget = widgets.DateInput(attrs={"type": "date"})
        form.fields["address"].widget = widgets.Textarea(attrs={"rows": 2})
        form.fields["others"].widget = widgets.Textarea(attrs={"rows": 2})
        return form


class EmployeeUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Employee
    fields = "__all__"
    success_message = "Запись успешно обновлена."

    def get_form(self):
        """add date picker in forms"""
        form = super(EmployeeUpdateView, self).get_form()
        form.fields["date_of_birth"].widget = widgets.DateInput(attrs={"type": "date"})
        form.fields["date_of_employment"].widget = widgets.DateInput(
            attrs={"type": "date"}
        )
        form.fields["address"].widget = widgets.Textarea(attrs={"rows": 2})
        form.fields["others"].widget = widgets.Textarea(attrs={"rows": 2})
        form.fields['photo'].widget = widgets.FileInput()
        return form


class EmployeeDeleteView(LoginRequiredMixin, DeleteView):
    model = Employee
    success_url = reverse_lazy("employee-list")


class EmployeeBulkUploadView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = EmployeeBulkUpload
    template_name = "employees/employee_upload.html"
    fields = ["csv_file"]
    success_url = "/employee/list"
    success_message = "Успешно загруженные сотрудники"


class DownloadCSVViewdownloadcsv(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="employee_template.csv"'

        writer = csv.writer(response)
        writer.writerow(
            [
                "registration_number",
                "surname",
                "firstname",
                "other_names",
                "gender",
                "parent_number",
                "address",
                "current_class",
            ]
        )

        return response
