from django import http
from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from owner.forms import *

# Create your views here.
@login_required
def home(request):
    return render(request, 'staff_home.html')

@login_required
def new_post(request):
    if request.method == "GET":
        pcf = PostCreationForm()
        return render(request, 'staff_post_creation.html', {'form': pcf})
    
    # If posted
    pcf = PostCreationForm(request.POST)
    if pcf.is_valid():
        return HttpResponse("Saving Data")
    return render(request, 'staff_post_creation.html', {'form': pcf})