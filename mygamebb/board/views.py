from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .filters import CommentFilter
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


def about(request):
    return render(request, 'board/about.html', {'menu': menu, 'title': 'О сайте'})

class AddBulletin(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddBulletinForm
    model = Bulletin
    template_name = 'board/addbulletin.html'
    # success_url = reverse_lazy('home')
    login_url = reverse_lazy('login')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление объявления")
        return dict(list(context.items()) + list(c_def.items()))

class EditBulletin(LoginRequiredMixin, DataMixin, UpdateView):
    form_class = AddBulletinForm
    model = Bulletin
    template_name = 'board/addbulletin.html'
    # success_url = reverse_lazy('home')
    login_url = reverse_lazy('login')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Редактирование объявления")
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

class AddReply(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddReplyForm
    model = Comment
    template_name = 'board/addreply.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('login')
    raise_exception = True


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

class ProfileList(DataMixin, ListView):
    model = Comment
    template_name = 'board/profile.html'
    context_object_name = 'comments'
    # allow_empty = False


    # def get_queryset(self):
    #     return Comment.objects.filter(bulletin__user=self.request.user.id)

    def get_queryset(self):
        queryset = Comment.objects.filter(bulletin__user=self.request.user.id)
        self.filterset = CommentFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     c_def = self.get_user_context(title='Мои объявления')
    #
    #     return dict(list(context.items()) + list(c_def.items()))


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
        c_def = self.get_user_context(title=context['bulletin'], flag=(self.object.user==self.request.user))
        return dict(list(context.items()) + list(c_def.items()))



def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

# class RegisterUser(DataMixin, CreateView):
#     form_class = RegisterUserForm
#     template_name = 'board/register.html'
#     success_url = reverse_lazy('login')
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title="Регистрация")
#         return dict(list(context.items()) + list(c_def.items()))
#
#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return redirect('home')

# class LoginUser(DataMixin, LoginView):
#     form_class = LoginUserForm
#     template_name = 'board/login.html'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title="Авторизация")
#         return dict(list(context.items()) + list(c_def.items()))
#
#     def get_success_url(self):
#         return reverse_lazy('home')


# def logout_user(request):
#     logout(request)
#     return redirect('login')

class CommentConfirm(UpdateView):
    form_class = ConfirmCommentForm
    model = Comment
    template_name = 'board/comment_confirm.html'
    success_url = reverse_lazy('profile')

class CommentDelete(DeleteView):
    model = Comment
    template_name = 'board/comment_delete.html'
    success_url = reverse_lazy('profile')

# @login_required
# def subscribe(request, pk):
#     user = request.user
#     category = Category.objects.get(id=pk)
#     category.subscribers.add(user)
#
#     message = 'Вы подписались на рассылку новостей категории'
#     return render(request, 'news/subscribe.html', {'category': category, 'message': message})

class NewsList(DataMixin, ListView):
    model = News
    template_name = 'board/news.html'
    context_object_name = 'news'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     c_def = self.get_user_context(title='Категория - ' + str(context['bulletins'][0].cat),
    #                                   cat_selected=context['bulletins'][0].cat_id)
    #     return dict(list(context.items()) + list(c_def.items()))

class ShowNew(DataMixin, DetailView):
    model = News
    template_name = 'board/new.html'
    context_object_name = 'new'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     c_def = self.get_user_context(title=context['bulletin'], flag=(self.object.user==self.request.user))
    #     return dict(list(context.items()) + list(c_def.items()))





