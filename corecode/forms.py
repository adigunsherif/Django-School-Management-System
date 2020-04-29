from django import forms
from django.forms import modelformset_factory

from .models import SiteConfig, AcademicTerm, AcademicSession, StudentClass, Subject

SiteConfigForm = modelformset_factory(SiteConfig, fields=('key', 'value',), extra=0)

AcademicTermForm = modelformset_factory(AcademicTerm, fields=('name',), can_delete=True, extra=0)

AcademicSessionForm = modelformset_factory(AcademicSession, fields=('name',), can_delete=True, extra=0)

StudentClassForm = modelformset_factory(StudentClass, fields=('name',), can_delete=True, extra=0)

SubjectForm = modelformset_factory(Subject, fields=('name',), can_delete=True, extra=0)

class CurrentSessionForm(forms.Form):
  current_session = forms.ModelChoiceField(queryset=AcademicSession.objects.all(), help_text='Click <a href="/sessions">here</a> to add new session')
  current_term = forms.ModelChoiceField(queryset=AcademicTerm.objects.all())
