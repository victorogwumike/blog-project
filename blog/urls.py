from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import SignUpView  # new

urlpatterns = [
    path("", views.home, name="home"),
    path("create/", views.create_post, name="create_post"),
    path("edit/<int:post_id>/", views.edit_post, name="edit_post"),
    path("signup/", SignUpView.as_view(), name="signup"),  # new
]
