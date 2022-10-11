from asyncio import Task
from django.contrib import messages
from django.shortcuts import redirect, render

from todo.models import Category, Todo
from .forms import CreateCategoryForm, CreateTodoForm
from django.contrib.auth.decorators import login_required


def landing_view(request):
    '''Home view'''
    return render(request, 'todo/landingPage.html')


@login_required(login_url='login_view')
def home(request):
    from django.db.models import Count
    '''Home view'''
    context = {}    
    categories = Category.objects.filter(created_by=request.user).annotate(num_count=Count('todo'))    
    todos = Todo.objects.filter(created_by=request.user,status = 'pending')
    from datetime import date
    context['categories'] = categories
    context['todos'] = todos
    return render(request, 'todo/homePage.html', context)


@login_required(login_url='login_view')
def add_category(request):
    '''Add category view'''
    data = request.POST
    data._mutable = True
    data['created_by'] = request.user
    form = CreateCategoryForm(data=data)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS,
                             'Category Added Successfully')
        return redirect('home_view')


@login_required(login_url='login_view')
def add_todo_task(request):
    '''Add Task view'''
    data = request.POST
    data._mutable = True
    data['created_by'] = request.user
    form = CreateTodoForm(data=data)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS,
                             'Task Added Successfully')
        return redirect('home_view')
    else:
        print(form.errors)
        messages.add_message(request, messages.WARNING,
                             'Process Failed')
        return redirect('home_view')


@login_required(login_url='login_view')
def edit_todo_task(request, id):
    '''edit task'''
    obj = Todo.objects.get(id=id)
    title = request.POST.get('title')
    description = request.POST.get('description')
    category = request.POST.get('category')
    scheduled_time = request.POST.get('scheduled_time') or obj.scheduled_time
    Todo.objects.filter(id=id).update(title=title, description=description,
                                      category=category, scheduled_time=scheduled_time)

    return redirect('home_view')


@login_required(login_url='login_view')
def complete_todo_task(request, id):
    '''Mark task as Completed'''
    Todo.objects.filter(id=id).update(status='completed')
    return redirect('home_view')


@login_required(login_url='login_view')
def delete_todo_task(request, id):
    '''Delete task'''
    Todo.objects.get(id=id).delete()
    return redirect('home_view')
