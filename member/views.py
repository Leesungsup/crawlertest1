from django.shortcuts import render
from .views import *
from .models import BoardMember
# Create your views here.
def register(request):
    if request.method == "GET":
        return render(request,'register.html')
    elif request.method == "POST":
        post=BoardMember()
        post.username    = request.POST.get('username', None)
        #print(username)
        post.password    = request.POST.get('password', None)
        #print(password)
        post.re_password = request.POST.get('re_password', None)
        #print(re_password)
        post.email  = request.POST.get('email', None)
        post.save()
        return render(request, 'register.html')