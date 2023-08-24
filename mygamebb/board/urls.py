from django.urls import path
from board.views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('addbulletin/', addbulletin, name='add_bulletin'),
    path('login/', login, name='login'),
    path('bulletin/<int:bul_id>/', show_bulletin, name='bulletin'),
    path('category/<int:cat_id>/', show_category, name='category')
]
