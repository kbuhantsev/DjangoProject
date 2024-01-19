from django.urls import URLPattern, path

from orders import views

app_name = "orders"

urlpatterns: list[URLPattern] = [
    path("create-order/", views.create_order, name="create_order"),
]

