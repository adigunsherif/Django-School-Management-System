from django.urls import path

from . import views

urlpatterns = [
  path('', views.IndexView.as_view(), name='home'),
  path('site-config', views.siteconfig_view, name='configs'),
  path('current-session/', views.current_session_view, name='current-session'),

  path('session/list/', views.SessionListView.as_view(), name='sessions'),
  path('session/create/', views.SessionCreateView.as_view(), name='session-create'),
  path('session/<int:pk>/update/',
       views.SessionUpdateView.as_view(), name='session-update'),
  path('session/<int:pk>/delete/',
       views.SessionDeleteView.as_view(), name='session-delete'),

  path('term/list/', views.TermListView.as_view(), name='terms'),
  path('term/create/', views.TermCreateView.as_view(), name='term-create'),
  path('term/<int:pk>/update/',
       views.TermUpdateView.as_view(), name='term-update'),
  path('term/<int:pk>/delete/',
       views.TermDeleteView.as_view(), name='term-delete'),

  path('class/list/', views.ClassListView.as_view(), name='classes'),
  path('class/create/', views.ClassCreateView.as_view(), name='class-create'),
  path('class/<int:pk>/update/',
       views.ClassUpdateView.as_view(), name='class-update'),
  path('class/<int:pk>/delete/',
       views.ClassDeleteView.as_view(), name='class-delete'),

  path('subject/list/', views.SubjectListView.as_view(), name='subjects'),
  path('subject/create/', views.SubjectCreateView.as_view(),
       name='subject-create'),
  path('subject/<int:pk>/update/',
       views.SubjectUpdateView.as_view(), name='subject-update'),
  path('subject/<int:pk>/delete/',
       views.SubjectDeleteView.as_view(), name='subject-delete'),

]
