from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title=models.CharField(max_length=400)
    content=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def get_absolute_url(self):
        return reverse("post-view",kwargs={"pk":self.pk})
    
    
class OK(models.Model):
    pass

