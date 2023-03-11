
from django.db import models
# from django.contrib.auth.models import User


# Create your models here.
class Students(models.Model):
   sname = models.CharField(max_length=50,null=True,blank=True)
   age = models.IntegerField()
   email = models.EmailField(max_length = 50,null=True,blank=True)
#    image = models.ImageField(upload_to='Posted_Images', blank=True, null=True,)
   
   def __str__(self):
          return self.sname


