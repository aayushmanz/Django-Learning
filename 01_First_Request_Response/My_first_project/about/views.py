from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def collegeinfo(request):
    return render(request, "webpage/index.html")

