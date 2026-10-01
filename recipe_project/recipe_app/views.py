from django.shortcuts import render

def recipes(request):

   if request.method == "POST": 
     data = request.POST
     

     recipe_image = request.FILES.get('recipe_img')
     recipe_name = data.get("recipe_name")
     recipe_desc = data.get("recipe_desc")

     print(recipe_name)
     print(recipe_desc)


   return render(request, 'recipe.html')
# Create your views here.
