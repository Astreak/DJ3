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


class PostView(ListView):
    model=Post
    template_name="blog/post.html"
    context_object_name="posts" # for getting off the default list object dtype
    ordering=["-date_posted"]
    

