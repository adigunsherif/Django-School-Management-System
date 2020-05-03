from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect, redirect

from corecode.models import AcademicSession, AcademicTerm
from students.models import Student

from .models import Result
from .forms import CreateResults, EditResults


def create_result(request):
  students = Student.objects.all()
  if request.method == 'POST':

    #after visiting the second page
    if 'finish' in request.POST:
      form = CreateResults(request.POST)
      if form.is_valid():
        subjects = form.cleaned_data['subjects']
        session = form.cleaned_data['session']
        term = form.cleaned_data['term']
        students = request.POST['students']
        results = []
        for student in students.split(','):
          stu = Student.objects.get(pk=student)
          for subject in subjects:
            check = Result.objects.filter(session=session, term=term,current_class=stu.current_class,subject=subject, student=stu).first()
            if not check:
              results.append(
                  Result(
                      session=session,
                      term=term,
                      current_class=stu.current_class,
                      subject=subject,
                      student=stu
                  )
              )
        Result.objects.bulk_create(results)
        return redirect('edit-results')

    #after choosing students
    id_list = request.POST.getlist('students')
    if id_list:
      form = CreateResults()
      studentlist = ','.join(id_list)
      return render(request, 'result/create_result_page2.html', {"students": studentlist, "form": form})
    else:
      messages.warning(request, "You didnt select any student.")
  return render(request, 'result/create_result.html', {"students": students})


def edit_results(request):
  if request.method == 'POST':
    form = EditResults(request.POST)
    print(form.errors)
    if form.is_valid():
      print(form.errors)
      form.save()
      messages.success(request, 'Results successfully updated')
      return redirect('edit-results')
  else:
    form = EditResults()
  return render(request, 'result/edit_results.html', {"formset": form})
