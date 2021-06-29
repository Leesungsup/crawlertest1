from django.shortcuts import render
from .views import *
# Create your views here.
def register(request):
    return render(request,'register.html')