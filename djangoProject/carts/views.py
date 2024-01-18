from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from goods.models import Products
from carts.models import Cart


@csrf_exempt
def cart_add(request, product_slug: str):
    product = Products.objects.get(slug=product_slug)
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)
        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)
    return redirect(request.META.get('HTTP_REFERER'))


def cart_change(request, product_slug: str):
    return None


def cart_remove(request, product_slug: str):
    return None
