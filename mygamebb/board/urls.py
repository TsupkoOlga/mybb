from django.urls import path
from board.views import *

urlpatterns = [
    path('', index),
    path('cats/', categories)
]
