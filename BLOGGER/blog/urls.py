from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name="blog-home"),
    path('post/',views.Post_view,name="blog-post")
        
]