from django.urls import path
from .views import PostView,PostDetails,PostCreate,PostUpdate,PostDelete
from . import views
urlpatterns=[
    path('',views.home,name="blog-home"),
    path('post/',PostView.as_view(),name="blog-post"),
    path('post/<int:pk>/',PostDetails.as_view(),name="post-view"),
    path('post/new/',PostCreate.as_view(),name="post-create"),
    path('post/<int:pk>/update',PostUpdate.as_view(),name="post-update"),
    path('post/<int:pk>/delete',PostDelete.as_view(),name="post-delete"),
    
    
    
        
]