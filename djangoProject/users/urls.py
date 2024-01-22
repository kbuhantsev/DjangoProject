from django.urls import URLPattern, path

from users import views

app_name = "users"  # pylint: disable=invalid-name

urlpatterns: list[URLPattern] = [
    path("login/", views.login, name="login"),
    path("registration/", views.registration, name="registration"),
    path("profile/", views.profile, name="profile"),
    path("logout/", views.logout, name="logout"),
    path("users-cart/", views.users_cart, name="users_cart"),
    path("password-change/", views.password_change, name="password_change"),
]
