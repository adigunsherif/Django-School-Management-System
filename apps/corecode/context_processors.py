from .models import AcademicSession, AcademicTerm, SiteConfig
from apps.employees.models import Employee


def site_defaults(request):
    current_session = AcademicSession.objects.get(current=True)
    current_term = AcademicTerm.objects.get(current=True)
    vals = SiteConfig.objects.all()
    employee_count = Employee.objects.count()
    contexts = {
        "current_session": current_session.name,
        "current_term": current_term.name,
        "employee_count": employee_count,
    }
    for val in vals:
        contexts[val.key] = val.value

    return contexts
