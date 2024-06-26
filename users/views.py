from django.shortcuts import render


def login(request):
    context = {
        'title': 'Home - Авторизация'
    }

    return render(request, 'users/login.html', context)


def register(request):
    context = {
        'title': 'Home - Регистрация'
    }

    return render(request, 'users/registration.html', context)


def profile(request):
    context = {
        'title': 'Home - Кабина'
    }

    return render(request, 'users/profile.html', context)


def logout(request):
    pass
