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
     
     
     
     # for creating the object structure for table
     recipe.objects.create(
     recipe_name = recipe_name,
     recipe_desc = recipe_desc,
     recipe_img = recipe_image
     )

     return redirect('/recipe/')

   # taking object to backend to front-end through context
   query_set = recipe.objects.all()
   context = {'recipe' : query_set}
   return render(request, 'recipe.html', context)




# Create your views here.
