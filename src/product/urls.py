from django.urls import path
from .views import product
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', product.ProductView.as_view(), name='product-list'),
]

