from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import widgets
from django.urls import reverse_lazy

from .models import Staff


class StaffListView(ListView):
    model = Staff


class StaffDetailView(DetailView):
    model = Staff
    template_name = "staffs/staff_detail.html"


class StaffCreateView(SuccessMessageMixin, CreateView):
    model = Staff
    fields = '__all__'
    success_message = 'New staff successfully added'

    def get_form(self):
        '''add date picker in forms'''
        form = super(StaffCreateView, self).get_form()
        form.fields['date_of_birth'].widget = widgets.DateInput(
            attrs={'type': 'date'})
        form.fields['date_of_admission'].widget = widgets.DateInput(attrs={
                                                                    'type': 'date'})
        form.fields['address'].widget = widgets.Textarea(attrs={'rows': 1})
        form.fields['others'].widget = widgets.Textarea(attrs={'rows': 1})
        return form


class StaffUpdateView(SuccessMessageMixin, UpdateView):
    model = Staff
    fields = '__all__'
    success_message = "Record successfully updated."

    def get_form(self):
        '''add date picker in forms'''
        form = super(StaffUpdateView, self).get_form()
        form.fields['date_of_birth'].widget = widgets.DateInput(
            attrs={'type': 'date'})
        form.fields['date_of_admission'].widget = widgets.DateInput(attrs={
                                                                    'type': 'date'})
        form.fields['address'].widget = widgets.Textarea(attrs={'rows': 1})
        form.fields['others'].widget = widgets.Textarea(attrs={'rows': 1})
        return form

class StaffDeleteView(DeleteView):
  model = Staff
  success_url = reverse_lazy('staff-list')
