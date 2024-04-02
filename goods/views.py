from django.core.paginator import Paginator
from django.shortcuts import render

from goods.models import Products


def catalog(request, category_slug):
    page = request.GET.get('page', 1)

    if category_slug == 'all':
        goods = Products.objects.all()
    else:
        goods = Products.objects.filter(category__slug=category_slug)

    paginator = Paginator(goods, 3)
    current_page = paginator.page(page)
    slug_url = category_slug

    context: dict = {
        'title': 'Home - Каталог',
        'goods': current_page,
        'slug_url': slug_url,
    }

    return render(request, 'goods/catalog.html', context)


def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)

    context = {
        'title': product.name,
        'product': product,
    }

    return render(request, 'goods/product.html', context)
