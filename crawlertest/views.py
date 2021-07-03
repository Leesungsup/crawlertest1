from django.shortcuts import render
from django.http import HttpResponse
def hello(request):
    html="<html><body>Hi</body></html>"
    return HttpResponse(html)
def home(request):
    return render(request,'home.html')
def htmltest(request):
    #기본템플릿 폴 1. admin 앱 2. 각 앱의 폴더에 있는 template폴더 3. 우리가 설정한폴더
    return render(request,'html.html')
def basetest(request):
    #기본템플릿 폴 1. admin 앱 2. 각 앱의 폴더에 있는 template폴더 3. 우리가 설정한폴더
    return render(request,'base.html')
def login(request):
    if request.method == "GET":
        return render(request,'login.html')
    elif request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username)
        print(password)
        res={}
        if not (username and password):
            res['error']='모든 값을 입력해주세요.'
        else:
            member=BoardMember.objects.get(username=username)
            print(member.password)
            print(check_password(member.password,password))
            if check_password(member.password,password):
                print(1)
                request.session['user']=member.id
                return redirect('/')
            else:
                res['error']='비밀번호가 다릅니다!'
        return render(request,'login.html',res)