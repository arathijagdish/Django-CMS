from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Create your views here.
def login(request):
    return render(request, 'login.html', {'form': AuthenticationForm()})

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