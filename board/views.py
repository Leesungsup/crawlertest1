from django.shortcuts import render,redirect
from .models import Board
from .forms import *
from member.models import BoardMember
# Create your views here.
def board_list(request):
    boards= Board.objects.all().order_by('-id')
    return render(request, 'board_list.html', {"boards":boards})
def board_write(request):
    if request.method =="POST":
        form=BoardForm(request.POST)
        if form.is_valid():
            user_id=request.session.get('user')
            member=BoardMember.objects.get(pk=user_id)
            print(member)
            board=Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer=member
            print(board.title)
            print(board.contents)
            board.save()
            return redirect('/board/board_list/')
    else:
        form=BoardForm()
    return render(request,'board_write.html',{'form':form})