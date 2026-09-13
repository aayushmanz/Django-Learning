from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse('Hello Ayush , you are at new journey !')
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse('hello ayush, this about page')

def contact(request):
    return HttpResponse("hello ayush, this for contact" )