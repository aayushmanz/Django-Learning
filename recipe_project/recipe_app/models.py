from django.db import models


class recipe(models.Model):
    recipe_name = models.CharField(max_length=100)
    recipe_desc = models.TextField()
    recipe_img = models.ImageField(upload_to='recipe_images/')

# Create your models here.
