
from django.urls import path
from .templates import views

urlpatterns = [
    
    path('', views.all_app, name='all_app'),

]