from django.urls import path

from .views import *

urlpatterns = [
  path('', index_view, name='home'),
  path('site-config', siteconfig_view, name='configs'),
  path('terms', academic_terms_view, name='terms'),
  path('sessions', academic_sessions_view, name='sessions'),
  path('classes', student_classes_view, name='classes'),
  path('subjects', subject_view, name='subjects'),
  path('current-session', current_session_view, name='current-session'),
  path('developer', developer, name='developer'),
]
