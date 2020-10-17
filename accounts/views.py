from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def login(request):
    return render(request, 'login.html', {'form': AuthenticationForm()})