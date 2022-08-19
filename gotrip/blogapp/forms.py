from django import forms
from .models import Post
from django_summernote.widgets import SummernoteWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['제목', '체크리스트1', '체크리스트2', '체크리스트3', '썸네일', '내용']
        widgets = {
            '내용': SummernoteWidget(),
        }
