from django.shortcuts import render, redirect
from .models import recipe


def recipes(request):

   if request.method == "POST": 
     data = request.POST
     

     recipe_image = request.FILES.get('recipe_img')
     recipe_name = data.get("recipe_name")
     recipe_desc = data.get("recipe_desc")

     print(recipe_name)
     print(recipe_desc)

     return redirect('/recipe/')


   query_set = recipe.objects.all()
   context = {'recipe' : query_set}
   return render(request, 'recipe.html', context)




# Create your views here.
