from django.urls import URLPattern, path

from carts import views

app_name = "carts"

urlpatterns: list[URLPattern] = [
    path("cart_add/<slug:product_slug>", views.cart_add, name="cart_add"),
    path("cart_change/<slug:product_slug>", views.cart_change, name="cart_change"),
    path("cart_remove/<slug:product_slug>", views.cart_remove, name="cart_remove")
]
