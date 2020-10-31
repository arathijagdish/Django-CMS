import os
from django.http import request
from django.http.response import Http404, HttpResponseNotFound
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.decorators import login_required
from owner.forms import *
from markdown import markdown

# Create your views here.
@login_required
def home(request):
    posts = Post.objects.filter(created_by=request.user)[:100]
    for p in posts:
        p.body = markdown(p.body)
    return render(request, 'staff_home.html', {'data': posts})

@login_required
def new_post(request):
    if request.method == "GET":
        pcf = PostCreationForm()
        return render(request, 'staff_post_creation.html', {'form': pcf})
    
    # If posted
    pcf = PostCreationForm(request.POST, request.FILES)
    if pcf.is_valid():
        post = pcf.save(commit=False)
        post.created_by = request.user
        post.save()
        return redirect("staff_home")
    return render(request, 'staff_post_creation.html', {'form': pcf})

@login_required
def delete_post(request, id):
    try:
        post = Post.objects.get(pk=id, created_by=request.user)
        if post.featured_image:
            if os.path.isfile(post.featured_image.path):
                os.remove(post.featured_image.path)
        post.delete()
        return redirect('staff_home')
    except:
        return HttpResponseNotFound()

@login_required
def edit_post(request, id):
    post = Post.objects.get(pk=id, created_by=request.user)
    if request.method == "GET":
        pcf = PostCreationForm(instance = post)
        return render(request, 'staff_post_edit.html', {'form': pcf})
    
    pcf = PostCreationForm(data = request.POST, instance=post, files=request.FILES)
    if pcf.is_valid():
        pcf.save()
        return redirect('staff_home')
    return render(request, 'staff_post_edit.html', {'form': pcf})
    
    
    
