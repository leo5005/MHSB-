from django import forms
from django.utils import timezone

class PostForm(forms.Form):
    title = forms.CharField(max_length=30, label='タイトル')
    content = forms.CharField(label='内容', widget=forms.Textarea())
    created = forms.DateTimeField(label='作成日', initial=timezone.now())
    picture = forms.ImageField(label='画像', required=False)