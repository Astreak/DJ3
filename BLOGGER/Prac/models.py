from django.db import models

class Artist(models.Model):
    fname=models.CharField(max_length=400);
    lname=models.CharField(max_length=500);
    instrument=models.CharField(max_length=200)
    def __str__(self):
        return f"{self.fname} {self.lname}";

class Music(models.Model):
    name=models.CharField(max_length=100),
    genre=models.CharField(max_length=400)
    def __str__(self):
        return f"{self.name}";



