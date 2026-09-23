from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def collegeinfo(request):
    student = [
        {'name' : 'ayush suthar', 'age' : 22},
        {'name' : 'komal vaishnav', 'age' : 21},
        {'name' : 'deepak patidar', 'age' : 19},
        {'name' : 'yo yo honey singh', 'age' : 41},
        {'name' : 'ayush singh', 'age' : 16},
        {'name' : 'rajat', 'age' : 22},
        {'name' : 'zeeshan', 'age' : 21},
        {'name' : 'hemi singh', 'age' : 27},
    ]
    return render(request, "webpage/index.html", context={'std' : student})

