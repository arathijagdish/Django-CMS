from django.http.response import HttpResponseBadRequest, HttpResponseNotFound
from owner.models import Post
from django.http import request
from accounts.views import login
from django.shortcuts import render, HttpResponse
from markdown import markdown
from owner.models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all().order_by('-created_on')[:20]
    return render(request, 'user_home.html', {'data': posts})

def about(request):
    return HttpResponse("About Us")

def viewpost(request, url):
    try:
        post = Post.objects.get(slug=url)
        post.body = markdown(post.body)
        return render(request, 'user-view-post.html', {'data': post})
    except:
        return HttpResponseNotFound()

def search(request):
    search = request.GET.get('s')
    if search:
        posts = Post.objects.filter(title__contains = search).order_by('-created_on')[:50]
        return render(request, 'user_home.html', {'data': posts})
    return HttpResponseBadRequest()