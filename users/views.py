from django.shortcuts import render, redirect
from account.models import *
from .forms import LoginUser
from django.contrib.auth import authenticate, login

def user_login(request):
    if request.method == 'POST':
        form = LoginUser(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(request,username=cd['username'],password=cd['password'])
            if user and user.is_active:
                login(request,user)
                return redirect('/')  
    else:
        form = LoginUser()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    return render(request, 'users/logout.html')
