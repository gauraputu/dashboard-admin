from django.urls import path
from .views import dashboard
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', dashboard.DashboardView.as_view(), name='dashboard'),
]

