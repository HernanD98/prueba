from django.db import models

# Create your models here.

class Banner(models.Model):
    banner_name = models.CharField(max_length=10, unique=True)
    slug = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=200, unique=True)
    images = models.ImageField(upload_to='photos/banners')

    def __str__(self):
        return self.banner_name
    

class HomeImage(models.Model):
    image_name = models.CharField(max_length=20, unique=True)
    slug = models.CharField(max_length=30, unique=True)
    description = models.TextField(max_length=250, unique=True)
    images = models.ImageField(upload_to='home/presentation')