from django.shortcuts import render

def all_app(request):
    return render(request, 'app/all_app.html')

# Create your views here.
