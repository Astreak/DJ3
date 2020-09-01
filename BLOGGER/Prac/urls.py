from django.urls import path
from . import views
from blog import views as blog_views
from users import views as u_views

urlpatterns=[
    path('',blog_views.home,name="prac-views"),
    path('register/',u_views.register,name="prac-register"),
    
    

]