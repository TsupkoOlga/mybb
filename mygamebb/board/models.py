from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



# class Author(models.Model):
    # user = models.OneToOneField(User, on_delete = models.CASCADE)

    # def __str__(self):
    #     return self.user.username



class Category(models.Model):
    name = models.CharField(max_length=63, unique=True)

    def __str__(self):
        return self.name.title()

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})



class Bulletin(models.Model):
    title = models.CharField(max_length=63)
    # time_in = models.DateTimeField(auto_now_add = True)
    content = models.TextField(default="Место для текста")
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)

    # def preview(self):
       # if len(self.content) < 125:
           # prw = self.content
       # else:
           # prw = self.content[:124] + '...'
       # return prw

    def __str__(self):
        return self.title.title()

    def get_absolute_url(self):
        return reverse('bulletin', kwargs={'bul_id': self.pk})
    #def __str__(self):
        #return f'{self.title.title()}: {self.content[:20]}'

    # def get_absolute_url(self):
       # return reverse('news_detail', args=[str(self.id)])

# class PostCategory(models.Model):
    # post = models.ForeignKey(Post, on_delete = models.CASCADE)
    # category = models.ForeignKey(Category, on_delete = models.CASCADE)

class Comment(models.Model):
    # time_in = models.DateTimeField(auto_now_add=True)
    reply = models.CharField(max_length=255)
    bulletin = models.ForeignKey(Bulletin, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    is_accept = models.BooleanField(default=False)
