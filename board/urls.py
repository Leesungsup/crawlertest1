from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('board_list/',board_list),
    path('board_write/',board_write),
]
