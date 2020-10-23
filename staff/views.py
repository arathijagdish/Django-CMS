from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from owner.forms import *

# Create your views here.
@login_required
def home(request):
    return render(request, 'staff_home.html')

@login_required
def new_post(request):
    pcf = PostCreationForm()
    return render(request, 'staff_post_creation.html', {'form': pcf})