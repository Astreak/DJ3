from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import datetime
class Account(models.Model):
   user=models.OneToOneField(User,on_delete=models.CASCADE);
   image=models.ImageField(default="default.jpg",upload_to="profile_pics")
   def __str__(self):
         return (f" {self.user.username} Profile");
   def save(self,*a,**k):
         super().save();
         I=Image.open(self.image.path);
         if I.height>300 or I.width>300:
               O=(300,300);
               I.thumbnail(O)
               I.save(self.image.path)
         
class Mees(models.Model):
      sen=models.OneToOneField(User,related_name="sender",on_delete=models.CASCADE)
      rec=models.ForeignKey(User,on_delete=models.CASCADE)
      
      def __str__(self):
            return f"{self.sen.username} is following {self.rec.username}"
      
      
   
class Person(models.Model):
      Age_range=(
           ("1-10","Noob"),
           ("10-20","Young"),
           ( "20-30","OK"),
           ("30-40","uncle"),
           ("40-50","lol: uncle"),
           ("50-100","hello::grandpa")
      )
      Fname=models.CharField(max_length=100)
      Lname=models.CharField(max_length=100)
      age=models.IntegerField()
      address=models.CharField(max_length=1000)
      Range=models.CharField(max_length=6,choices=Age_range,default="30-40")
      date=models.DateField(default=datetime.datetime.now())
      
      def __str__(self):
            return f"Mr. {self.Fname} {self.Lname}";
