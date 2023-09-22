from django.contrib import admin

from .models import *

class BulletinAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'cat')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'reply', 'bulletin', 'user', 'is_accept')
    list_display_links = ('id', 'bulletin')
    search_fields = ('reply',)
    list_editable = ('is_accept',)

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Bulletin, BulletinAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(News, NewsAdmin)

