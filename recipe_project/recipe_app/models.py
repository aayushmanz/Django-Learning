from django.db import models
# from django.contrib.auth import User


class recipe(models.Model):
    recipe_name = models.CharField(max_length=100)
    recipe_desc = models.TextField()
    recipe_img = models.ImageField(upload_to='recipe_images/')

# Create your models here.


class login(models.Model):
    
    username = models.CharField(max_length=30, null=False)
    password = models.CharField(max_length=40)
    