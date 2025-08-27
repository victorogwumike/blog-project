from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPost


def home(request):
    posts = BlogPost.objects.all().order_by("-created_at")
    return render(request, "blog/home.html", {"posts": posts})

def create_post(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        BlogPost.objects.create(title=title, content=content, author=request.user if request.user.is_authenticated else None)
        return redirect("home")
    return render(request, "blog/create_post.html")

def edit_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if request.method == "POST":
        post.title = request.POST["title"]
        post.content = request.POST["content"]
        post.save()
        return redirect("home")
    return render(request, "blog/edit_post.html", {"post": post})
