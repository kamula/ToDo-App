from django.shortcuts import render


def home(request):
    '''Home view'''
    return render(request, 'todo/index.html')
