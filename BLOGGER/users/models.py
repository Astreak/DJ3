from django.db import models
from django.contrib.auth.models import User
from PIL import Image
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
      rec=models.OneToOneField(User,related_name="rec",on_delete=models.CASCADE)
      
      def __str__(self):
            return f"{self.sen.username} is following {self.rec.username}"
      
      
   
