from .models import AcademicTerm, AcademicSession

def site_defaults(request):
  current_session = AcademicSession.objects.get(current=1)
  current_term = AcademicTerm.objects.get(current=1)

  contexts = {
      "current_session": current_session.name,
      "current_term": current_term.name
  }

  return contexts
