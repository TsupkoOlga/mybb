from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .models import *
from .utils import *


class BulletinList(DataMixin, ListView):
    model = Bulletin
    template_name = 'board/index.html'
    context_object_name = 'bulletins'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(c_def.items()))


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

class AddBulletin(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddBulletinForm
    template_name = 'board/addbulletin.html'
    # success_url = reverse_lazy('home')
    login_url = reverse_lazy('login')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление объявления")
        return dict(list(context.items()) + list(c_def.items()))


# def addbulletin(request):
#     if request.method == 'POST':
#         form = AddBulletinForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = AddBulletinForm()
#     return render(request, 'board/addbulletin.html', {'form': form, 'menu': menu, 'title': 'Добавление объявления'})

# def login(request):
#     return HttpResponse('Авторизация')

class CategoryList(DataMixin, ListView):
    model = Bulletin
    template_name = 'board/index.html'
    context_object_name = 'bulletins'
    allow_empty = False

    def get_queryset(self):
        return Bulletin.objects.filter(cat__id=self.kwargs['cat_id'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категория - ' + str(context['bulletins'][0].cat),
                                      cat_selected=context['bulletins'][0].cat_id)
        return dict(list(context.items()) + list(c_def.items()))


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

class ShowBulletin(DataMixin, DetailView):
    model = Bulletin
    template_name = 'board/bulletin.html'
    context_object_name = 'bulletin'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['bulletin'])
        return dict(list(context.items()) + list(c_def.items()))




def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'board/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'board/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')
