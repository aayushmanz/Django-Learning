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

    """
     python manage.py shell

     from mainapp.models import * 
     
     # We are using the CRUD functions :

     



    # CREATE : 

     c1 = car(brand_name = "TATA", model_name = "siara", speed = "180")
     c2 = car(brand_name = "Mahendra", model_name = "Scorpio", speed = "150")
     c1.save()
     c2.save()
     
     car_dictionary = {"brand_name" : "Suzuki", "model_name" : "aulto", "speed" : "100"}

     car.objects.create(**car_dictionary)

     



    # READ :
      
     car.objects.all() # we can se all cars now easily !

     # output :
     # <QuerySet [<car: TATA Siara>]>


     for i in cars:
       print(f'This brand car name is {i.brand_name} and model is {i.model_name} with the speed of {i.speed}')

     # output :
     # This brand car name is TATA and model is Siara with the speed of 180
     # This brand car name is Mahendra and model is Scorpio with the speed of 150
     # This brand car name is Suzuki and model is aulto with the speed of 100  
     
     car.objects.get(id = 1)  # get method use 

     # output :
     #  <car: TATA Siara>
     
     car.objects.filter(id = 1) # filter method use

     # output :
     #  <QuerySet [<car: TATA Siara>]>

     

     

     # UPDATE :
     
     # There are two ways to perform update function through get method and filter method 

     # get :
     # this is much longer process to perform 

     c1 = car.objects.get(id = 1) # id = 1 is belong to TATA
       
     c1.brand_name = "BMV"     # updated brand name      
     c1.model_name = "m5"      # updated model name
     c1.speed = "210"          # updated speed

     c1.save()                 # save update


     # filter :
     # short way

     car.objects.filter(id = 1).update(brand_name = "BMW") # thats it


     

     # DELETE :
     # we can use filter and get function for delete 
     
     # use get :
     car.objects.get(id = 1).delete()


     # use filter :
     car.objects.filter(id = 1).delete()

     # if we want to delete all data :
     car.objects.all().delete()

   """
    


    