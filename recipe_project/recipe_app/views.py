from django.shortcuts import render, redirect
from .models import recipe


def recipes(request):

   if request.method == "POST":
     recipe_image = request.FILES.get("recipe_img")
     recipe_name = request.POST.get("recipe_name")
     recipe_desc = request.POST.get("recipe_desc")

     recipe.objects.create(
         recipe_name=recipe_name,
         recipe_desc=recipe_desc,
         recipe_img=recipe_image,
     )

     return redirect("/recipe/")

   # taking object to backend to front-end through context
   query_set = recipe.objects.all()
   context = {'recipe' : query_set}
   return render(request, 'recipe.html', context)


def delete_recipe(request, id):
  query = recipe.objects.get(id = id)
  query.delete()
  
  return redirect('/recipe/')

  

# Create your views here.
