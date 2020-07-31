from django.urls import path
from . import views
from blog import views as blog_views
urlpatterns=[
    path('',blog_views.home),
    path("register/",views.register,name="users-register"),
    path("profile/",views.Profile,name="user-profile"),
    path("msg/",views.msg,name="user-msg"),
    path("info/",views.persons,name="user-info"),
]