from django import forms
from . models import Category, Todo


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'created_by']


class AddTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'scheduled_time']
