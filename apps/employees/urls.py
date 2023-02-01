from django.urls import path

from .views import (
    DownloadCSVViewdownloadcsv,
    EmployeeBulkUploadView,
    EmployeeCreateView,
    EmployeeDeleteView,
    EmployeeDetailView,
    EmployeeListView,
    EmployeeUpdateView,
)

urlpatterns = [
    path("list", EmployeeListView.as_view(), name="employee-list"),
    path("<int:pk>/", EmployeeDetailView.as_view(), name="employee-detail"),
    path("create/", EmployeeCreateView.as_view(), name="employee-create"),
    path("<int:pk>/update/", EmployeeUpdateView.as_view(), name="employee-update"),
    path("<int:pk>/delete/", EmployeeDeleteView.as_view(), name="employee-delete"),
    path("upload/", EmployeeBulkUploadView.as_view(), name="employee-upload"),
    path("download-csv/", DownloadCSVViewdownloadcsv.as_view(), name="download-csv"),
]
