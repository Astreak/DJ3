from django.shortcuts import render
from django.http import HttpResponse

def home(req):
    return render(req,"home.html")

# Create your views here.
