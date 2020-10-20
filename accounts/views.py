from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Create your views here.
def login(request):
    return render(request, 'login.html', {'form': AuthenticationForm()})

def register(request):
    return render(request, 'register.html', {'form': UserCreationForm()})