from django.shortcuts import render
from django.http import HttpResponse
import datetime

from products.models import Categories


def index(request) -> HttpResponse:
    
    categories = Categories.objects.all()
    
    context = {
        'title': 'home',
        'content': 'Main page',
        'categories': categories,
       
        'datetime': datetime.datetime.now(),
    }
    return render(request, 'main/index.html', context)



def about(request) -> HttpResponse:
    context = {
        'title': 'About',
        'content': 'About page',
        'about_as': 'About as'
    
    }
    return render(request, 'main/about.html', context)