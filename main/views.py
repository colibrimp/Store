from django.shortcuts import render
from django.http import HttpResponse
import datetime


# Create your views here.
# Controller

def index(request) -> HttpResponse:
    context: dict[str, str] = {
        'title': 'home',
        'content': 'Main page',
       
        'datetime': datetime.datetime.now()
    }
    return render(request, 'main/index.html', context)



def about(request) -> HttpResponse:
    context: dict[str, str] = {
        'title': 'About',
        'content': 'About page',
        'about_as': 'About as'
    
    }
    return render(request, 'main/about.html', context)