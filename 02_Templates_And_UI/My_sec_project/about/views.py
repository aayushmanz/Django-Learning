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


def subject_page(request):
    context = {"page" : "subject"}
    return render(request, "webpage/subject.html", context)

def contact_page(request):
    context = {"page" : "contact"}
    return render(request, "webpage/contact.html", context)


