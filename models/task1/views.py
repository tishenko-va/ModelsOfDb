
from django.shortcuts import render
from .forms import UserRegister
from django.http import HttpResponse
from .models import *
from django.contrib.auth.hashers import make_password
from django.core.paginator import Paginator

def main_page(request):
    return render(request, 'first_task/main_page.html')

def shop_page(request):
    games = Game.objects.all()
    context = {
        'games': games
    }

    return render(request, 'first_task/shop_page.html', context)


def cart_page(request):
    return render(request, 'first_task/cart_page.html')

users = ['Anton', 'Gleb', 'Alina']

def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif Buyer.objects.filter(
                    name=username).exists():  # Проверяем существование пользователя в таблице Buyer
                info['error'] = 'Пользователь уже существует'
            else:
                hashed_password = make_password(password)
                Buyer.objects.create(name=username, password=hashed_password, age=age)
                return render(request, 'first_task/registration_page.html', {'message': f'Приветствуем, {username}!'})


        info['form'] = form
    else:
        form = UserRegister()

    info['form'] = form
    return render(request, 'first_task/registration_page.html', info)


def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if password != repeat_password:
            info['error'] = "Пароли не совпадают"
            return HttpResponse('Пароли не совпадают')
        elif int(age) < 18:
            info['error'] = "Вы должны быть старше 18"
            return HttpResponse('Вы должны быть старше 18')
        elif Buyer.objects.filter(name=username).exists():
            info['error'] = "Пользователь уже существует"
            return HttpResponse('Пользователь уже существует')
        else:
            hashed_password = make_password(password)
            Buyer.objects.create(name=username, password=hashed_password, age=age)
            info['welcome_message'] = f"Приветствуем, {username}!"
            return HttpResponse(f"Приветствуем, {username}!")

    return render(request, 'first_task/registration_page.html', context=info)

def news(request):
    news_list = News.objects.all().order_by('-date')
    paginator = Paginator(news_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'news': page_obj,
    }
    return render(request, 'first_task/news.html', context)

