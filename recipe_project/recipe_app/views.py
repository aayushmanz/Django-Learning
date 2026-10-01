from django.shortcuts import render

def recipes(request):
    recipe_data = request.POST()
    return render(request, 'recipe.html')
# Create your views here.
