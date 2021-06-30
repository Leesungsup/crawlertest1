from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import BoardMember
from django.contrib.auth.hashers import make_password,check_password
from .form import *
# Create your views here.
def home(request):
    user_id=request.session.get('user')
    if user_id:
        member = BoardMember.objects.get(pk=user_id)# 아까 세션에 id 를 넣어놓았었다. 세션의 user 키에 넣어 두었던게 id 값이였다.
        return redirect('/')
    return HttpResponse('login fail')
def register(request):
    if request.method == "GET":
        return render(request,'register.html')
    elif request.method == "POST":
        username    = request.POST.get('username', None)
        #print(username)
        email  = request.POST.get('email', None)
        password    = request.POST.get('password', None)
        #print(password)
        re_password = request.POST.get('re_password', None)
        #print(re_password)
        res={}
        if not (username and email and password and re_password):
            res['error']='모든 값을 입력하세요.'
        if password != re_password:
            res['error']='비밀번호가 다릅니다.'
        else:
            post=BoardMember(
                username=username,
                password=make_password(password),
                email=email)
            post.save()
            return redirect('.')
        return render(request, 'register.html',res)
def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('/')
def login(request):
    if request == "POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user_id
            return redirect('/')
    else:
        form = LoginForm()
    return render(request,'login.html',{'form': form})