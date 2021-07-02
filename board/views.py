from django.shortcuts import render,redirect
from .models import Board
from .forms import *
from member.models import BoardMember
from django.http import Http404
# Create your views here.
def board_list(request):
    boards= Board.objects.all().order_by('-id')
    return render(request, 'board_list.html', {"boards":boards})
def board_write(request):
    if not request.session.get('user'):
        return redirect('member/login/')
    if request.method =="POST":
        form=BoardForm(request.POST)
        if form.is_valid():
            user_id=request.session.get('user')
            member=BoardMember.objects.get(pk=user_id)
            board=Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer=member
            board.save()
            return redirect('/board/board_list/')
    else:
        form=BoardForm()
    return render(request,'board_write.html',{'form':form})
def board_detail(request,pk):
    try:
        board=Board.objects.get(pk=pk)
    except board.DoesNotExist:
        raise Http404('게시글이 없습니다.')
    return render(request,'board_detail.html',{'board':board})