from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

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
    
    
class PostDetails(DetailView):
    model=Post #model we care about
    template_name="blog/details.html"
    context_object_name="posts" # for getting off the default list object dtype

class PostCreate(LoginRequiredMixin,CreateView):
    model=Post
    fields=['title','content']
    def form_valid(self,form):
        form.instance.author=self.request.user;
        return super().form_valid(form)
        
        

class PostUpdate(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    fields=["title","content"]
    def form_valid(self,form):
        form.instance.author=self.request.user;
        return super().form_valid(form)
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False

class PostDelete(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    success_url="/blog/post"
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False
    


    
