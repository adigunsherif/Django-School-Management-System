from django.urls import path

from .views import all_results_view, create_result, edit_results

urlpatterns = [
    path("create/", create_result, name="create-result"),
    path("edit-results/", edit_results, name="edit-results"),
    path("view/all", all_results_view, name="view-results"),
]
