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

from .models import Doc, DocBulkUpload

from .forms import (
    DocForm
)



class DocListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Doc
    template_name = "docs/doc_list.html"

    """ def get_context_data(request):
        #context = super().get_context_data(**kwargs)
        #context["form"] = EmployeeForm()
        context ={}
        context["employees"] = Employee.objects.all()
        return context """

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["docs"] = Doc.objects.all()
        return context

#def home(request):
#   employee_list = Employee.objects.all()
#   return render(request, 'home.html', {'employee_list': employee_list})


class DocDetailView(LoginRequiredMixin, DetailView):
    model = Doc
    fields = "__all__"
    template_name = "docs/doc_detail.html"

    def get_context_data(self, **kwargs):
        context = super(DocDetailView, self).get_context_data(**kwargs)
    #    context["payments"] = Invoice.objects.filter(employee=self.object)
        return context


class DocCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Doc
    fields = "__all__"
    success_message = "Новый сотрудник успешно добавлен"

    def get_form(self):
        """add date picker in forms"""
        form = super(DocCreateView, self).get_form()
        form.fields["date_of_issue"].widget = widgets.DateInput(attrs={"type": "date", "date_format":"%d.%m.%Y"})
        form.fields["date_of_expiry"].widget = widgets.DateInput(attrs={"type": "date", "date_format":"d.m.Y"})
        form.fields["address"].widget = widgets.Textarea(attrs={"rows": 2})
        form.fields["others"].widget = widgets.Textarea(attrs={"rows": 2})
        return form


class DocUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Doc
    fields = "__all__"
    success_message = "Запись успешно обновлено"

    def get_form(self):
        """add date picker in forms"""
        form = super(DocUpdateView, self).get_form()
        form.fields["date_of_issue"].widget = widgets.DateInput(attrs={"type": "date"})
        form.fields["date_of_expiry"].widget = widgets.DateInput(attrs={"type": "date"})
        form.fields["address"].widget = widgets.Textarea(attrs={"rows": 2})
        form.fields["others"].widget = widgets.Textarea(attrs={"rows": 2})
        return form


class DocDeleteView(LoginRequiredMixin, DeleteView):
    model = Doc
    success_url = reverse_lazy("doc-list")


class DocBulkUploadView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = DocBulkUpload
    template_name = "docs/doc_upload.html"
    fields = ["csv_file"]
    success_url = "/doc/list"
    success_message = "Успешно загруженные сотрудники"


class DownloadCSVViewdownloadcsv(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="doc_template.csv"'

        writer = csv.writer(response)
        writer.writerow(
            [
                "serial",
                "number",
                "date_of_issue",
                "date_of_expiry",
                "doc_type",
            ]
        )

        return response
