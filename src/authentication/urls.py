from django.urls import path
from .views import login
from django.contrib.auth.views import LoginView

urlpatterns = [
    # path('activate-account/<uidb64>/<token>/', activation.activate_account, name='activate-account'),

    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    # path('logout/', views.logout_user, name='logout'),
    # path('forgot-password/', views.forgot_password.index, name='forgot-password'),

    # path('test/', views.forgot_password.test_template, name='test'),
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', views.forgot_password.CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),

    # path('', dashboard.index, name="superapp")
]

