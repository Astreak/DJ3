from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import UserRegisterForm
def register(req):
    if req.method=="POST":
        form=UserRegisterForm(req.POST);
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get("username");
            messages.success(req,f"Welcome to the family  MR.{username} you can login now ");
            return redirect("login")
    else:
        form=UserRegisterForm()
        
    return render(req,"users/register.html",{'form':form});

@login_required
def Profile(req):
    return render(req,"users/profile.html");

    
