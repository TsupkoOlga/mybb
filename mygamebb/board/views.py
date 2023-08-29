from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView

from .forms import *
from .models import *

menu = [{'title': 'На главную', 'url_name': 'home'},
        {'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить объявление', 'url_name': 'add_bulletin'},
        {'title': 'Войти', 'url_name': 'login'}
]

class BulletinList(ListView):
    model = Bulletin
    template_name = 'board/index.html'
    context_object_name = 'bulletins'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Bulletin.objects.all()


# def index(request):
#     bulletins = Bulletin.objects.all()
#     cats = Category.objects.all()
#     context = {'bulletins': bulletins,
#                'cats': cats,
#                'menu': menu,
#                'title': 'Главная страница',
#                'cat_selected': 0
#     }
#     return render(request, 'board/index.html', context=context)

def about(request):
    return render(request, 'board/about.html', {'menu': menu, 'title': 'О сайте'})

def addbulletin(request):
    if request.method == 'POST':
        form = AddBulletinForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddBulletinForm()
    return render(request, 'board/addbulletin.html', {'form': form, 'menu': menu, 'title': 'Добавление объявления'})

def login(request):
    return HttpResponse('Авторизация')

class CategoryList(ListView):
    model = Bulletin
    template_name = 'board/index.html'
    context_object_name = 'bulletins'
    allow_empty = False

    def get_queryset(self):
        return Bulletin.objects.filter(cat__id=self.kwargs['cat_id'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - ' + str(context['bulletins'][0].cat)
        context['menu'] = menu
        context['cat_selected'] = context['bulletins'][0].cat_id
        return context


# def show_category(request, cat_id):
#     cats = Category.objects.all()
#     bulletins = Bulletin.objects.filter(cat_id=cat_id)
#
#     if len(bulletins) == 0:
#         raise Http404()
#
#     context = {'bulletins': bulletins,
#                'cats': cats,
#                'menu': menu,
#                'title': 'Объявления по категориям',
#                'cat_selected': cat_id
#                }
#     return render(request, 'board/index.html', context=context)

# def show_bulletin(request, bul_id):
#     bulletin = get_object_or_404(Bulletin, pk= bul_id)
#     context = {'bulletin': bulletin,
#                'menu': menu,
#                'title': bulletin.title,
#                'cat_selected': bulletin.cat_id
#                }
#     return render(request, 'board/bulletin.html', context=context)

class ShowBulletin(DetailView):
    model = Bulletin
    template_name = 'board/bulletin.html'
    # pk_url_kwarg = 'bulletin.id'
    context_object_name = 'bulletin'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['bulletin']
        context['menu'] = menu
        return context




def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
