from django import forms
from django.forms import modelformset_factory
from corecode.models import AcademicSession, AcademicTerm, StudentClass

from .models import Result

class CreateResults(forms.Form):
  session = forms.ModelChoiceField(queryset=AcademicSession.objects.all())
  term = forms.ModelChoiceField(queryset=AcademicTerm.objects.all())



