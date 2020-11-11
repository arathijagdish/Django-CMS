from accounts.models import User
import django
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import RegistrationForm

# Create your views here.
def user_login(request):
    if request.method == "GET":
        return render(request, 'login.html', {'form': AuthenticationForm()})
    
    # If POST
    lf = AuthenticationForm(data=request.POST)
    if lf.is_valid():
        username = lf.cleaned_data['username']
        password = lf.cleaned_data['password']

        user = authenticate(request, username=username, password=password)
        login(request, user)
        if user.is_superuser:
            pass
        return redirect('staff_home')
    
    # If invalid
    return render(request, 'login.html', {'form': lf})


def register(request):
    if request.method == "GET":
        return render(request, 'register.html', {'form': RegistrationForm()})
    
    # If the request method is POST
    ucf = RegistrationForm(request.POST)
    if ucf.is_valid():
        user = User()
        user.name = ucf.cleaned_data['name']
        user.email = ucf.cleaned_data['email']
        user.set_password(ucf.cleaned_data['password'])
        user.save() # Saving the user to database
        return redirect('login')

    # If the form is invalid
    return render(request, 'register.html', {'form': ucf})

def user_logout(request):
    logout(request)
    return redirect('login')