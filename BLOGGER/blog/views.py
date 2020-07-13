from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.decorators import login_required
@login_required
def home(req):
    return render(req,"blog/home.html")

def about(req):
    return HttpResponse("<h1><center> Blog HOme </center></h1>")
def login(req):
    return render(req,"blog/login.html");
def register(req):
    return render(req,"blog/register.html");
