from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages

from .models import SiteConfig, AcademicSession, AcademicTerm, StudentClass, Subject
from .forms import SiteConfigForm, AcademicTermForm, AcademicSessionForm, StudentClassForm, SubjectForm, CurrentSessionForm

# Create your views here.
@login_required
def index_view(request):
  return render(request, 'corecode/index.html')

@login_required
def siteconfig_view(request):
  """ Site Config View """
  if request.method == 'POST':
    form = SiteConfigForm(request.POST)
    print(form.errors)
    if form.is_valid():
      form.save()
      messages.success(request, 'Configurations successfully updated')
      return HttpResponseRedirect('site-config')
  else:
    form = SiteConfigForm(queryset=SiteConfig.objects.all())

  context = {"formset": form, "title": "Configuration"}
  return render(request, 'corecode/siteconfig.html', context)

@login_required
def academic_terms_view(request):
  """ Academic Terms View """
  if request.method == 'POST':
    form = AcademicTermForm(request.POST)
    if form.is_valid() and form.has_changed():
      form.save()
      messages.success(request, 'Terms successfully saved')
      return HttpResponseRedirect('terms')
  else:
    form = AcademicTermForm(queryset=AcademicTerm.objects.all())

  context = {"formset": form, "title": "Terms"}
  return render(request, 'corecode/mgt_form.html', context)

@login_required
def academic_sessions_view(request):
  """ Academic Sessions View """
  if request.method == 'POST':
    form = AcademicSessionForm(request.POST)
    if form.is_valid() and form.has_changed():
      form.save()
      messages.success(request, 'Terms successfully saved')
      return HttpResponseRedirect('sessions')
  else:
    form = AcademicSessionForm(queryset=AcademicSession.objects.all())

  context = {"formset": form, "title": "Sessions"}
  return render(request, 'corecode/mgt_form.html', context)

@login_required
def student_classes_view(request):
  """ Classes View """
  if request.method == 'POST':
    form = StudentClassForm(request.POST)
    if form.is_valid() and form.has_changed():
      form.save()
      messages.success(request, 'Terms successfully saved')
      return HttpResponseRedirect('classes')

  else:
    form = StudentClassForm(queryset=StudentClass.objects.all())

  context = {"formset": form, "title": "Classes"}
  return render(request, 'corecode/mgt_form.html', context)

@login_required
def subject_view(request):
  """ Subject View """
  if request.method == 'POST':
    form = SubjectForm(request.POST)

    if form.is_valid() and form.has_changed():
      form.save()
      messages.success(request, 'Terms successfully saved')
      return HttpResponseRedirect('subjects')

  else:
    form = SubjectForm(queryset=Subject.objects.all())

  context = {"formset": form, "title": "Subjects"}
  return render(request, 'corecode/mgt_form.html', context)

@login_required
def current_session_view(request):
  """ Current SEssion and Term """
  if request.method == 'POST':
    form = CurrentSessionForm(request.POST)
    if form.is_valid():
      session = form.cleaned_data['current_session']
      term = form.cleaned_data['current_term']
      AcademicSession.objects.filter(name=session).update(current=True)
      AcademicSession.objects.exclude(name=session).update(current=False)
      AcademicTerm.objects.filter(name=term).update(current=True)
      AcademicTerm.objects.exclude(name=term).update(current=False)

  else:
    form = CurrentSessionForm(initial={
      "current_session": AcademicSession.objects.get(current=True),
      "current_term": AcademicTerm.objects.get(current=True)
    })


  return render(request, 'corecode/current_session.html', {"form":form})

@login_required
def developer(request):
  """ Developer """
  return render(request, 'corecode/developer.html')
