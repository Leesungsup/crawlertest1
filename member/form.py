from django.contrib.auth.hashers import check_password,make_password
from django import forms
from .models import BoardMember
from django.core.exceptions import ObjectDoesNotExist
class LoginForm(forms.Form):
    # 입력받을 값 두개
    username = forms.CharField(error_messages={
        'required':'아이디를 입력하세요!'
    },max_length=100, label="사용자이름")
    password = forms.CharField(error_messages={
        'required':'비밀번호를 입력하세요!'
    },widget=forms.PasswordInput, max_length=100, label="비밀번호")
    # 처음 값이 들어왔다 는 검증 진행
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        if username and password:
            try:
                print(username)
                member = BoardMember.objects.get(username=username)
                print(4)
            except BoardMember.DoesNotExist:
                print(3)
                self.add_error('username','아이디가 없습니다!')
                return
            if not (password==member.password):
                self.add_error('password', '비밀번호가 다릅니다!')
            else:
                self.user_id = member.id
