from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns=[
    path('register/',register),
    path('login/',login),
    path('logout/,',logout),
    path('',home),
]