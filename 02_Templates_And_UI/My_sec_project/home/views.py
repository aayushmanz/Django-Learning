from django.shortcuts import render
from django.http import HttpResponse

def welcome(response):
    return HttpResponse("""<h1>Ayush Suthar</h1>
    <p>this page is welcome page for my team coderiots</p>
    <hr>
    <h3>Welcome to my page ;)</h3>
    """)
