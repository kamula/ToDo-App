from django.shortcuts import render


def landing_view(request):
    '''Home view'''
    return render(request, 'todo/landingPage.html')

def home(request):
    '''Home view'''
    return render(request, 'todo/homePage.html')