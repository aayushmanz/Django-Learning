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
   
   if request.GET.get("search"):
          # print(request.GET.get("search"))
          query_set = query_set.filter(recipe_name__icontains = request.GET.get('search'))
   
   context = {'recipe' : query_set}
   return render(request, 'recipe.html', context)


def delete_recipe(request, id):
  query = recipe.objects.get(id = id)
  query.delete()
  
  return redirect('/recipe/')



def update_recipe(request, id):
  queries = recipe.objects.get(id = id)
  
  if request.method == 'POST':
    data = request.POST
    
    queries.recipe_name = data.get('recipe_name')
    queries.recipe_desc = data.get('recipe_desc')
    
    if request.FILES.get('recipe_image'):
      queries.recipe_img = request.FILES.get('recipe_image')
      
    queries.save()  
  
    return redirect('/recipe/')
  
  context = {'recipe': queries}
  return render(request, 'update_recipe.html', context)


  

# Create your views here.
