from django.shortcuts import render

# from django.http import HttpResponse



def catalog(request):
    context = {
        "title": "Catalog",
        "categories": []
          
    }
    return render(request, "products/catalog.html", context)


def product(request):

    return render(request, "products/product.html")
