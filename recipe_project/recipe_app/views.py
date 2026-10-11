from django.shortcuts import render, redirect
from .models import recipe
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


@ login_required(login_url='/login/')
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

@ login_required(login_url='/login/')
def delete_recipe(request, id):
  query = recipe.objects.get(id = id)
  query.delete()
  
  return redirect('/recipe/')




@ login_required(login_url='/login/')
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





def login_page(request):
   if request.method == 'POST':
     username = request.POST.get('username')
     password = request.POST.get('password')
     
     check_user = authenticate(request, username = username, password=password)
     
     
     if check_user != None:
       login(request, check_user)
       print('U r verified !')
       return redirect('/recipe/')
       
     else:
       print('invaild user name and password !')  
       
     
     print(username)
     print(password)
  
   return render(request, "login.html")
 





def register_page(request):
  
  if request.method == "POST":
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    
    print("this is registration !")
    print(username)
    print(password)
    
    
    if User.objects.filter(username = username).exists():
      
      print('user already exist try different username !')
    
    
    else:  
    
        new_user = User.objects.create_user(
            username = username,
            password = password
          )
      
        new_user.save()
        print("congrates U r our new user, Mr" , new_user.username)
    
  return render(request, "register.html")  

# Create your views here.
