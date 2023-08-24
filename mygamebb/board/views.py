from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import *

menu = [{'title': 'На главную', 'url_name': 'home'},
        {'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить объявление', 'url_name': 'add_bulletin'},
        {'title': 'Войти', 'url_name': 'login'}
]

def index(request):
    cats = Category.objects.all()
    context = {'cats': cats,
               'menu': menu,
               'title': 'Категории:',
               'cat_selected': 0
    }
    return render(request, 'board/index.html', context=context)

def about(request):
    return render(request, 'board/about.html', {'menu': menu, 'title': 'О сайте'})

def addbulletin(request):
    return HttpResponse('Добавление объявления')

def login(request):
    return HttpResponse('Авторизация')


def show_category(request, cat_id):
    return HttpResponse(f'Статьи в категории {cat_id}')

def show_bulletin(request, bul_id):
    return HttpResponse(f'Отображение объявления с id = {bul_id}')






def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
