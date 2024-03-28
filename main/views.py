from django.shortcuts import render

from goods.models import Categories


def index(reqeust):
    categories = Categories.objects.all()

    context: dict = {
        'title': 'Home - Главная',
        'content': "Магазин мебели HOME",
        'categories': categories,
    }

    return render(reqeust, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Home - О нас',
        'content': "О нас",
        'text_on_page': "Текст о том почему этот магазин такой классный, и какой хороший товар."
    }

    return render(request, 'main/about.html', context)
