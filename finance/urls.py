from django.urls import path

from .views import InvoiceListView, InvoiceDeleteView, InvoiceDetailView,InvoiceUpdateView,ReceiptCreateView, ReceiptUpdateView

urlpatterns = [
    path('list/', InvoiceListView.as_view(), name='invoice-list'),
    path('<int:pk>/', InvoiceDetailView.as_view(), name='invoice-detail'),
    path('<int:pk>/update/', InvoiceUpdateView.as_view(), name='invoice-update'),
    path('<int:pk>/delete/', InvoiceDeleteView.as_view(), name='invoice-delete'),
    path('receipt/create', ReceiptCreateView.as_view(), name='receipt-create'),
    path('receipt/<int:pk>/update/', ReceiptUpdateView.as_view(), name='receipt-update'),
    path('receipt/<int:pk>/update/', ReceiptUpdateView.as_view(), name='receipt-update'),
]
