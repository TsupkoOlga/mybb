from django.urls import path
from board.views import *

urlpatterns = [
    path('', BulletinList.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addbulletin/', addbulletin, name='add_bulletin'),
    path('login/', login, name='login'),
    path('bulletin/<int:pk>/', ShowBulletin.as_view(), name='bulletin'),
    path('category/<int:cat_id>/', CategoryList.as_view(), name='category')
]
