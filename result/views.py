from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect, redirect

from corecode.models import AcademicSession, AcademicTerm
from students.models import Student
from .models import Result
from .forms import CreateResults

def create_result(request):
  initials = {"session":AcademicSession.objects.get(current=True), "term": AcademicTerm.objects.get(current=True)}
  if request.method == 'POST':
    form = CreateResults(request.POST, initial=initials)
    if form.is_valid():
      session = form.cleaned_data['session']
      term = form.cleaned_data['term']
      students = Student.objects.filter(current_status='active')
      results = []
      for student in students:
        if student.subjects_offered.all():
          for subject in student.subjects_offered.all():
            results.append(Result(
                student=student,
                session=session,
                term=term,
                current_class=student.current_class,
                subject=subject
            ))

      create = Result.objects.bulk_create(results)
      messages.success(request, '{} results successfully created.'.format(len(create)))
      link = '/result/create-page/?session={}&term={}'.format(session, term)
      return HttpResponseRedirect(link)

  else:
    form = CreateResults(initial=initials)
  return render(request, 'result/create_result.html', {"form":form})


def create_result_page(request):
  return redirect('create-result')
