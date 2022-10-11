from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_view, name='landing_view'),
    path('home', views.home, name='home_view'),
    path('categories', views.add_category, name='add_category_view'),
    path('todos', views.add_todo_task, name='add_todo_task_view'),
    path('todos/edit/<uuid:id>', views.edit_todo_task, name='edit_todo_task_view'),
    path('todos/delete/<uuid:id>', views.delete_todo_task, name='delete_todo_task_view'),
    path('todos/complete/<uuid:id>', views.complete_todo_task, name='complete_todo_task_view'),
]
