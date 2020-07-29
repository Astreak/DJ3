from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Post
from django.contrib.auth.decorators import login_required


@login_required
def home(req):
    
    return render(req,"blog/home.html")

@login_required
def Post_view(req):
    context={
        "posts":Post.objects.all()
    }
    return render(req,"blog/post.html",context);
    

def about(req):
    return HttpResponse("<h1><center> Blog HOme </center></h1>")
def login(req):
    return render(req,"blog/login.html");
def register(req):
    return render(req,"blog/register.html");


