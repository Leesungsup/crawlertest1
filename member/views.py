from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import BoardMember
from django.contrib.auth.hashers import make_password,check_password
from .form import *
from django import forms
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def home(request):
    user_id=request.session.get('user')
    if user_id:
        member = BoardMember.objects.get(pk=user_id)# 아까 세션에 id 를 넣어놓았었다. 세션의 user 키에 넣어 두었던게 id 값이였다.
        return redirect('/')
    return HttpResponse('login fail')
def test(request):
    return HttpResponse("test")
@csrf_exempt
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
            return redirect('/')
        return render(request, 'register.html',res)
def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('/')
@csrf_exempt
def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        print(2)
        # 폼 객체, 폼 클래스를 만들 때 괄호에 POST 데이터를 담아준다.
        # POST 안에 있는 데이터가 form 변수에 들어간다.
        if form.is_valid(): # 장고 폼에서 제공하는 검증 함수 is_valid()
            print(3)
            request.session['user']=form.user_id
            print(form.user_id)
            # session_code 검증
            return redirect('/')
    else:
        form = LoginForm()
        # 빈 클래스 변수를 만든다.
    return render(request, 'login.html', {'form':form})