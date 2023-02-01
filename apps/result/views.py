from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView, View

from apps.employees.models import Employee

from .forms import CreateResults, EditResults
from .models import Result


@login_required
def create_result(request):
    employees = Employee.objects.all()
    if request.method == "POST":

        # after visiting the second page
        if "finish" in request.POST:
            form = CreateResults(request.POST)
            if form.is_valid():
                subjects = form.cleaned_data["subjects"]
                session = form.cleaned_data["session"]
                term = form.cleaned_data["term"]
                employeesloyees = request.POST["employees"]
                results = []
                for employee in employees.split(","):
                    stu = Employee.objects.get(pk=employee)
                    if stu.current_class:
                        for subject in subjects:
                            check = Result.objects.filter(
                                session=session,
                                term=term,
                                current_class=stu.current_class,
                                subject=subject,
                                employee=stu,
                            ).first()
                            if not check:
                                results.append(
                                    Result(
                                        session=session,
                                        term=term,
                                        current_class=stu.current_class,
                                        subject=subject,
                                        employee=stu,
                                    )
                                )

                Result.objects.bulk_create(results)
                return redirect("edit-results")

        # after choosing employees
        id_list = request.POST.getlist("employees")
        if id_list:
            form = CreateResults(
                initial={
                    "session": request.current_session,
                    "term": request.current_term,
                }
            )
            employeelist = ",".join(id_list)
            return render(
                request,
                "result/create_result_page2.html",
                {"employees": employeelist, "form": form, "count": len(id_list)},
            )
        else:
            messages.warning(request, "You didnt select any employee.")
    return render(request, "result/create_result.html", {"employee": employees})


@login_required
def edit_results(request):
    if request.method == "POST":
        form = EditResults(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Results successfully updated")
            return redirect("edit-results")
    else:
        results = Result.objects.filter(
            session=request.current_session, term=request.current_term
        )
        form = EditResults(queryset=results)
    return render(request, "result/edit_results.html", {"formset": form})


class ResultListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        results = Result.objects.filter(
            session=request.current_session, term=request.current_term
        )
        bulk = {}

        for result in results:
            test_total = 0
            exam_total = 0
            subjects = []
            for subject in results:
                if subject.employee == result.employee:
                    subjects.append(subject)
                    test_total += subject.test_score
                    exam_total += subject.exam_score

            bulk[result.employee.id] = {
                "employee": result.employee,
                "subjects": subjects,
                "test_total": test_total,
                "exam_total": exam_total,
                "total_total": test_total + exam_total,
            }

        context = {"results": bulk}
        return render(request, "result/all_results.html", context)
