from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Account,Mees,Person

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField();
    
    class Meta:
        model=User
        fields=["username","email","password1",'password2'];

class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField();
    
    class Meta:
        model=User
        fields=["username","email"];

class AccountUpdateForm(forms.ModelForm):
    class Meta:
        model=Account
        fields=["image"]
        
class MSG(forms.ModelForm):
    class Meta:
        model=Mees
        fields=["sen","rec"]
        
class PRSN(forms.ModelForm):
    class Meta:
        model=Person
        fields="__all__"

        