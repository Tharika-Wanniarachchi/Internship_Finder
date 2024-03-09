from django.db import models
import uuid

# Create your models here.

class Company(models.Model):
    #id = models.AutoField()
    name = models.CharField(max_length=100)
    description = models.TextField(null =True,blank=True)
    date = models.DateTimeField(auto_now_add = True)
    logo = models.ImageField(null =True,blank=True,upload_to='logos/')  # Field for the company logo
    banner = models.ImageField(null =True,blank=True,upload_to='banners/')  # Field for the company banner
    id = models.UUIDField(default = uuid.uuid4,primary_key=True , editable = False ,unique=True)
    city =models.CharField(max_length=100,null =True,blank=True)
    country =models.CharField(max_length=100,null =True,blank=True)
    email = models.EmailField(null =True,blank=True)
    mobileNumber =models.CharField(max_length=20,null =True,blank=True)

    def __str__(self):
        return self.name
