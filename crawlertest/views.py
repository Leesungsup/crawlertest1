from django.shortcuts import render
from django.http import HttpResponse
def hello(request):
    html="<html><body>Hi</body></html>"
    return HttpResponse(html)
def htmltest(request):
    #기본템플릿 폴 1. admin 앱 2. 각 앱의 폴더에 있는 template폴더 3. 우리가 설정한폴더
    return render(request,'html.html')
