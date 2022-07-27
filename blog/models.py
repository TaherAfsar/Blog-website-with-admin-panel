
from datetime import date
from distutils.command.upload import upload
from email.mime import image
from django.db import models
from django.forms import CharField

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    date = models.DateField(auto_now=True)
    
