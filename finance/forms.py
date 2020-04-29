from django import forms
from django.forms import ModelForm, inlineformset_factory, formset_factory

from corecode.models import AcademicSession, AcademicTerm, StudentClass
from .models import *


class InvoiceCreateForm(ModelForm):
  class Meta:
    model = Invoice
    fields = ['session', 'term', 'class_for']


InvoiceItemFormset = inlineformset_factory(Invoice, InvoiceItem, fields=(
    'description', 'amount'), extra=2, can_delete=True)
InvoiceItemFormsetUpdate = inlineformset_factory(
    Invoice, InvoiceItem, fields=('description', 'amount'), extra=0, can_delete=True)


class InvoiceSearchForm(forms.Form):
  session = forms.ModelChoiceField(
      queryset=AcademicSession.objects.all(), required=False)
  term = forms.ModelChoiceField(queryset=AcademicTerm.objects.all(), required=False)
  class_for = forms.ModelChoiceField(
      label="Class", queryset=StudentClass.objects.all(), required=False)


InvoiceReceiptFormSet = inlineformset_factory(
    Invoice, Receipt, fields=('amount_paid', 'date_paid', 'comment'), extra=0, can_delete=True
)
