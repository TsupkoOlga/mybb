from django.urls import path
from board.views import *

urlpatterns = [
    path('', BulletinList.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addbulletin/', AddBulletin.as_view(), name='add_bulletin'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('bulletin/<int:pk>/', ShowBulletin.as_view(), name='bulletin'),
    path('category/<int:cat_id>/', CategoryList.as_view(), name='category')
]
