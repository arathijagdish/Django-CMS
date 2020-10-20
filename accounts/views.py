import django
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Create your views here.
def login(request):
    if request.method == "GET":
        return render(request, 'login.html', {'form': AuthenticationForm()})
    
    # If POST
    lf = AuthenticationForm(data=request.POST)
    if lf.is_valid():
        username = lf.cleaned_data['username']
        password = lf.cleaned_data['password']

        user = authenticate(request, username=username, password=password)
        login(user)
        return HttpResponse("Authentication completed")
    
    # If invalid
    return render(request, 'login.html', {'form': lf})


def register(request):
    if request.method == "GET":
        return render(request, 'register.html', {'form': UserCreationForm()})
    
    # If the request method is POST
    ucf = UserCreationForm(request.POST)
    if ucf.is_valid():
        ucf.save() # Saving the user to database
        return redirect('login')

    # If the form is invalid
    return render(request, 'register.html', {'form': ucf})