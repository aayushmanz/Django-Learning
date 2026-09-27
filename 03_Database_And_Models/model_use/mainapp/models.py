from django.db import models

# Create your models here.


class student(models.Model):

    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    rollno = models.IntegerField()
    age = models.IntegerField(default=18)
    email = models.EmailField()
    address = models.TextField(null=True, blank=True)

    def __str__(self):
            return self.name

class car(models.Model):
    brand_name = models.CharField(max_length=30)
    model_name = models.CharField(max_length=30)
    speed = models.IntegerField(default=50)

    def __str__(self):
         return self.brand_name + " " + self.model_name


    


    