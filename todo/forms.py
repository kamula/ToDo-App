from django import forms
from . models import Category, Todo


class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'created_by']


class CreateTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['created_by','title', 'category','description', 'scheduled_time']
