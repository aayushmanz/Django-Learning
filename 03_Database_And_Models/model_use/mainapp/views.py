from django.shortcuts import render

def home_page(request):
    context = { 'name' : 'Home'}
    return render(request, "index.html", context)

def about_page(request):
    context = { 'name' : 'About'}
    return render(request, 'about.html', context)

def contact_page(request):
    context = { 'name' : 'Contact'}
    return render(request, 'contact.html', context)