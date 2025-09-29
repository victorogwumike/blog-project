from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPost
from django.contrib.auth.forms import UserCreationForm  # new
from django.urls import reverse_lazy  # new
from django.views.generic.edit import CreateView  # new
from django.contrib.auth.decorators import login_required



class SignUpView(CreateView):  # new
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def home(request):
    posts = BlogPost.objects.all().order_by("-created_at")
    return render(request, "blog/home.html", {"posts": posts})

@login_required
def create_post(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        BlogPost.objects.create(title=title, content=content)  # 🔹 removed author
        return redirect("home")
    return render(request, "blog/create_post.html")

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if request.method == "POST":
        post.title = request.POST["title"]
        post.content = request.POST["content"]
        post.save()
        return redirect("home")
    return render(request, "blog/edit_post.html", {"post": post})
