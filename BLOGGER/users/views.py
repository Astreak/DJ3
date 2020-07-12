from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
def Register(req):
    if req.method=="POST":
        form=UserRegisterForm(req.POST);
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get("username");
            messages.success(req,f"HELLO MR.{username}");
            return redirect("blog-home")
    else:
        form=UserRegisterForm()
        
    return render(req,"users/register.html",{'form':form});

    
