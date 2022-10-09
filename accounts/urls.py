from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register', views.register, name='register_view'),
    path('login', auth_views.LoginView.as_view(template_name = 'accounts/Login.html'), name='login_view'),
    path('logout', auth_views.LogoutView.as_view(template_name = 'accounts/Logout.html'), name='logout_view'),
]
