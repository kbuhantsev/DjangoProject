from django.urls import URLPattern, path

from goods import views

app_name = "goods"  # pylint: disable=invalid-name

urlpatterns: list[URLPattern] = [
    path("<slug:category_slug>", views.catalog, name="index"),
    path("product/<slug:product_slug>/", views.product, name="product"),
]
