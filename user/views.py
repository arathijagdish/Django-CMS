from accounts.views import login
from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'user_home.html')

def about(request):
    return HttpResponse("About Us")