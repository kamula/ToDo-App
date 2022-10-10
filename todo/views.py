from django.contrib import messages
from django.shortcuts import redirect, render

from todo.models import Category
from .forms import CreateCategoryForm, CreateTodoForm
from django.contrib.auth.decorators import login_required


def landing_view(request):
    '''Home view'''
    return render(request, 'todo/landingPage.html')


@login_required(login_url='login_view')
def home(request):
    '''Home view'''
    context = {}
    categories = Category.objects.filter(created_by=request.user)
    context['categories'] = categories
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
    '''Home view'''
    return render(request, 'todo/homePage.html')
