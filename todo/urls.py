from django.urls import path
from . import views

urlpatterns = [
    path('',views.landing_view,name='landing_view'),
    path('home',views.home,name='home_view'),
    path('categories',views.add_category,name='add_category_view'),
]
