from django.db.models import Count

from .models import *

menu = [{'title': 'Новости', 'url_name': 'news'},
        {'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить объявление', 'url_name': 'add_bulletin'},
]

class DataMixin:
    paginate_by = 2
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('bulletin'))

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(2)

        context['menu'] = user_menu

        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context