from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Products


# Create your views here.
def catalog(request) -> HttpResponse:
    goods = Products.objects.all()
    context = {
        "title": "Home - Каталог",
        "goods": goods,
    }
    return render(request, "goods/catalog.html", context)


def product(request, product_slug) -> HttpResponse:

    finded_product = Products.objects.get(slug=product_slug)

    context = {
        'product' : finded_product
    }

    return render(request, "goods/product.html", context=context)
