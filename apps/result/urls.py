from django.urls import path

from .views import create_result, edit_results, all_results_view

urlpatterns = [
  path('create/', create_result, name='create-result'),
  path('edit-results/', edit_results, name='edit-results'),
  path('view/all', all_results_view, name='view-results'),
]
