from django.db.models import F

from .models import AcademicSession, AcademicTerm, SiteConfig
from apps.employees.models import Employee


def site_defaults(request):
    current_session = AcademicSession.objects.get(current=True)
    current_term = AcademicTerm.objects.get(current=True)
    vals = SiteConfig.objects.all()
    active_employee_count = Employee.objects.filter(current_status='active').count() # Get all employees with status 'active'
    contexts = {
        "current_session": current_session.name,
        "current_term": current_term.name,
        "active_employee_count": active_employee_count,
    }
    for val in vals:
        contexts[val.key] = val.value

    return contexts
