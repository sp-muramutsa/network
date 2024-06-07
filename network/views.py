from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.views.decorators.http import require_POST
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import User

from .forms import *


def index(request):
    posts = Post.objects.all().order_by("-created_at")
    return render(request, "network/index.html", {
        'posts': posts
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

def new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post.objects.create(
                author = request.user,
                title = form.cleaned_data["title"],
                content = form.cleaned_data["content"],
            )
        return HttpResponseRedirect(reverse("index"))    
    else:
        return render(request, "network/new.html", {
            'form': PostForm()
        }) 

def profile(request, username):
    if request.method == "GET":
        user = request.user
        networker = User.objects.filter(username=username).first()
        posts = Post.objects.filter(author=networker).order_by("-created_at")
        is_signed_in = not user.is_anonymous
        is_profile_owner = networker == user
        followers = networker.followers.all()
        is_following = user in followers
        followers_count = networker.followers_count()
        following_count = networker.following_count()
        

        return render(request, "network/profile.html", {
            'networker': networker,
            'posts': posts,
            'is_signed_in': is_signed_in,
            'is_profile_owner': is_profile_owner,
            'is_following': is_following,
            'followers_count': followers_count,
            'following_count': following_count
        })

@login_required
@require_POST
def follow_unfollow(request, username):
    user = request.user
    networker = User.objects.filter(username=username).first()

    if "follow" in request.POST:
        networker.followers.add(user)

    elif "unfollow" in request.POST:
        networker.followers.remove(user)

    return redirect(reverse('profile', args=[networker.username]))
    


