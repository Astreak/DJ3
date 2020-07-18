from django.shortcuts import render,redirect
from django.contrib.auth.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *
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
    if req.method=="POST":
        f1=UserUpdateForm(req.POST,instance=req.user)
        f2=AccountUpdateForm(req.POST,req.FILES,instance=req.user.account)
        if f1.is_valid() and f2.is_valid():
            f1.save()
            f2.save()
            return redirect("user-profile")
    else:
        f1=UserUpdateForm(instance=req.user)
        f2=AccountUpdateForm(instance=req.user.account)
        
    context={
        "f1":f1,
        "f2":f2
    }
    return render(req,"users/profile.html",context);

    
