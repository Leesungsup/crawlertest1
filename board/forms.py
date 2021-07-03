from django.contrib.auth.hashers import check_password
from django import forms
def min_length_3_validator(value):
	if len(value) < 3:
		raise forms.ValidationError('3글자 이상 입력해주세요')
class BoardForm(forms.Form):
    # 입력받을 값 두개
    title = forms.CharField(error_messages={
        'required':'제목을 입력하세요'
    },max_length=100, label="게시글 제목",validators=[min_length_3_validator])
    contents = forms.CharField(error_messages={
        'required':'내용을 입력하세요.'
    },widget=forms.Textarea, label="게시글 내용",validators=[min_length_3_validator])
class BoardUpdateForm(forms.Form):
    # 입력받을 값 두개
    title = forms.CharField(error_messages={
        'required':'제목을 입력하세요'
    },max_length=100, label="게시글 제목",validators=[min_length_3_validator])
    contents = forms.CharField(error_messages={
        'required':'내용을 입력하세요.'
    },widget=forms.Textarea, label="게시글 내용",validators=[min_length_3_validator])