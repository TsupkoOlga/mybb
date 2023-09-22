
from django.http import HttpResponseNotFound
from django.shortcuts import render
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

    def get_queryset(self):
        queryset = Comment.objects.filter(bulletin__user=self.request.user.id)
        self.filterset = CommentFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


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


class CommentConfirm(UpdateView):
    form_class = ConfirmCommentForm
    model = Comment
    template_name = 'board/comment_confirm.html'
    success_url = reverse_lazy('profile')

class CommentDelete(DeleteView):
    model = Comment
    template_name = 'board/comment_delete.html'
    success_url = reverse_lazy('profile')


class NewsList(DataMixin, ListView):
    model = News
    template_name = 'board/news.html'
    context_object_name = 'news'


class ShowNew(DataMixin, DetailView):
    model = News
    template_name = 'board/new.html'
    context_object_name = 'new'





