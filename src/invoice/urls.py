from django.urls import path
from .views import invoice
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', invoice.InvoiceView.as_view(), name='invoice-list'),
]

