from django.urls import path

from .views import create_result, create_result_page

urlpatterns = [
  path('create/', create_result, name='create-result'),
  path('create-page/', create_result_page, name='create-resdult'),
]
