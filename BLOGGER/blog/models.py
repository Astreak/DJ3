from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title=models.CharField(max_length=400)
    content=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)

class OK(models.Model):
    pass

