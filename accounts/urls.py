from django.urls import path
from . import views

urlpatterns = [
    path('register',views.register,name='register_view'),
    path('login',views.login,name='login_view'),
]