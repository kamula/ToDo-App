from django.shortcuts import render

def register(request):
    '''User registration view'''
    return render(request, 'accounts/Register.html')


def login(request):
    '''Login View'''
    return render(request, 'accounts/Login.html')
