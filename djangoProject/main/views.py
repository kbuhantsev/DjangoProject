from django.shortcuts import render
from django.http import HttpResponse

from goods.models import Categories


# Create your views here.
def index(request) -> HttpResponse:
    categories = Categories.objects.all()

    context = {
        "title": "Home - Главная",
        "content": "Магазин мебели HOME",
        "categories": categories,
    }
    return render(request, "main/index.html", context)


def about(request) -> HttpResponse:
    context = {
        "title": "Home - О нас",
        "content": "О нас",
        "text_on_page": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Modi qui iure reprehenderit. Exercitationem sequi consequatur cupiditate deleniti nobis! Provident eius facilis a, quisquam laudantium aspernatur odit tenetur error at possimus architecto totam necessitatibus nam fugiat odio ex. Impedit ea, beatae dicta fugiat quos ab, deleniti temporibus quam quaerat, recusandae aperiam!",
    }
    return render(request, "main/about.html", context)
