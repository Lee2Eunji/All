from django import forms
from .models import Board

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['writer', 'body']
        label = {
            'writer': '제목',
            'body': '내용 작성'
        }