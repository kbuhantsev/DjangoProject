from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import get_list_or_404, render

from goods.models import Products


# Create your views here.
def catalog(request, category_slug, page=1) -> HttpResponse:
    if category_slug == "all":
        goods = Products.objects.all()
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    paginator = Paginator(goods, 3)
    current_page = paginator.page(page)

    context = {
        "title": "Home - Каталог",
        "goods": current_page,
        "slug_url": category_slug,
    }
    return render(request, "goods/catalog.html", context)


def product(request, product_slug) -> HttpResponse:
    finded_product = Products.objects.get(slug=product_slug)
    context = {"product": finded_product}

    return render(request, "goods/product.html", context=context)
