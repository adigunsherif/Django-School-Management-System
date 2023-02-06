from django.urls import path

from .views import (
    DownloadCSVViewdownloadcsv,
    DocBulkUploadView,
    DocCreateView,
    DocDeleteView,
    DocDetailView,
    DocListView,
    DocUpdateView,
)

urlpatterns = [
    path("list", DocListView.as_view(), name="doc-list"),
    path("<int:pk>/", DocDetailView.as_view(), name="doc-detail"),
    path("create/", DocCreateView.as_view(), name="doc-create"),
    path("<int:pk>/update/", DocUpdateView.as_view(), name="doc-update"),
    path("<int:pk>/delete/", DocDeleteView.as_view(), name="doc-delete"),
    path("upload/", DocBulkUploadView.as_view(), name="doc-upload"),
    path("download-csv/", DownloadCSVViewdownloadcsv.as_view(), name="download-csv"),
]
