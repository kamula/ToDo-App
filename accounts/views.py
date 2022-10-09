from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def register(request):
    '''User registration view'''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)        
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'Account Created successfully')
            return redirect('login_view')
        else:
            messages.add_message(request,messages.WARNING,form.error_messages)
            return redirect('register_view')
    else:
        form = UserCreationForm()
        context = {
            'form':form
        }        
    return render(request, 'accounts/Register.html',context)


def login(request):
    '''Login View'''
    return render(request, 'accounts/Login.html')
