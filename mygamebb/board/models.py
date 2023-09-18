from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



# class Author(models.Model):
    # user = models.OneToOneField(User, on_delete = models.CASCADE)

    # def __str__(self):
    #     return self.user.username



class Category(models.Model):
    name = models.CharField(max_length=63, unique=True, verbose_name='Имя категории')

    def __str__(self):
        return self.name.title()

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']

class Bulletin(models.Model):
    title = models.CharField(max_length=63, verbose_name='Заголовок')
    # time_in = models.DateTimeField(auto_now_add = True, verbose_name='Заголовок')
    content = RichTextField(verbose_name='Текст объявления')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    # def preview(self):
       # if len(self.content) < 125:
           # prw = self.content
       # else:
           # prw = self.content[:124] + '...'
       # return prw

    def __str__(self):
        return self.title.title()

    def get_absolute_url(self):
        return reverse('bulletin', args=[str(self.id)])

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-id']
    #def __str__(self):
        #return f'{self.title.title()}: {self.content[:20]}'

    # def get_absolute_url(self):
       # return reverse('news_detail', args=[str(self.id)])

# class PostCategory(models.Model):
    # post = models.ForeignKey(Post, on_delete = models.CASCADE)
    # category = models.ForeignKey(Category, on_delete = models.CASCADE)

class Comment(models.Model):
    time_in = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    reply = models.CharField(max_length=255, verbose_name='Отклик')
    bulletin = models.ForeignKey(Bulletin, on_delete=models.CASCADE, verbose_name='Объявление')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    is_accept = models.BooleanField(default=False, verbose_name='Принят')

    class Meta:
        verbose_name = 'Отклик'
        verbose_name_plural = 'Отклики'
        ordering = ['id']
