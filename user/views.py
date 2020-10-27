from django.http.response import HttpResponseNotFound
from owner.models import Post
from django.http import request
from accounts.views import login
from django.shortcuts import render, HttpResponse
from markdown import markdown

# Create your views here.
def home(request):
    return render(request, 'user_home.html')

def about(request):
    return HttpResponse("About Us")

def viewpost(request, url):
    try:
        post = Post.objects.get(slug=url)
        post.body = markdown(post.body)
        return render(request, 'user-view-post.html', {'data': post})
    except:
        return HttpResponseNotFound()