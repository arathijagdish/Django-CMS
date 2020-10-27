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
    pcf = PostCreationForm(request.POST)
    if pcf.is_valid():
        post = pcf.save(commit=False)
        post.created_by = request.user
        post.save()
        return redirect("staff_home")
    return render(request, 'staff_post_creation.html', {'form': pcf})