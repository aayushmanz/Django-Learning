from django.contrib import admin
from .models import student

class std_admin(admin.ModelAdmin):
     list_display =  ('id', 'name', 'age', 'rollno', 'address')

admin.site.register(student, std_admin)
# Register your models here.
