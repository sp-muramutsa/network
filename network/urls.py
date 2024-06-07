
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new", views.new, name="new"),
    path("profile/<str:username>", views.profile, name="profile"),
    path("follow_unfollow/<str:username>", views.follow_unfollow, name="follow_unfollow"),
    path("following", views.following, name="following")
]
