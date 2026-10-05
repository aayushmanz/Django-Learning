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


def search_recipe(request, id):
  query = recipe.objects.get(id = id)
  
  if query.method == 'POST':
    data = request.POST
    
    query.recipe_name = data.get('recipe_name')
    query.recipe_desc = data.get('recipe_desc')
    
    if recipe_image:
      query.recipe_image = request.FILES.get('recipe_image')
      
    query.save()  
  
  return redirect('/recipe/')

  

# Create your views here.
