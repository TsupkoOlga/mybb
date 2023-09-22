from django.urls import path
from board.views import *

urlpatterns = [
    path('', BulletinList.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addbulletin/', AddBulletin.as_view(), name='add_bulletin'),
    path('bulletin/<int:pk>/edit/', EditBulletin.as_view(), name='edit_bulletin'),
    path('bulletin/<int:pk>/', ShowBulletin.as_view(), name='bulletin'),
    path('bulletin/<int:pk>/leavereply/', AddReply.as_view(), name='add_reply'),
    path('category/<int:cat_id>/', CategoryList.as_view(), name='category'),
    path('accounts/profile/', ProfileList.as_view(), name='profile'),
    path('accounts/profile/reply/confirm/<int:pk>', CommentConfirm.as_view(), name='confirm'),
    path('accounts/profile/reply/delete/<int:pk>', CommentDelete.as_view(), name='comment_delete'),
    path('news/', NewsList.as_view(), name='news'),
    path('news/<int:pk>/', ShowNew.as_view(), name='new'),

]
