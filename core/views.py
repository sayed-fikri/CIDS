from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'core/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'core/loginuser.html', {'form':AuthenticationForm(), 'error':'Username and password did not match'})
        else:
            login(request, user)
            return redirect('information:homepage')

@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('loginuser')
