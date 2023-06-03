from django import forms
from .models import Post_1,Post_2,Post_3,Post_4,Comment_1,Comment_2,Comment_3,Comment_4

class PostForm_1(forms.ModelForm):
   class Meta:
       model = Post_1
       exclude = ('created',)
       
class CommentForm_1(forms.ModelForm):
    class Meta:
        model = Comment_1
        exclude = ('target', 'created_at')
       
class PostForm_2(forms.ModelForm):
   class Meta:
       model = Post_2
       exclude = ('created',)

class CommentForm_2(forms.ModelForm):
    class Meta:
        model = Comment_2
        exclude = ('target', 'created_at')
       
class PostForm_3(forms.ModelForm):
   class Meta:
       model = Post_3
       exclude = ('created',)

class CommentForm_3(forms.ModelForm):
    class Meta:
        model = Comment_3
        exclude = ('target', 'created_at')
       
class PostForm_4(forms.ModelForm):
   class Meta:
       model = Post_4
       exclude = ('created',)
       
class CommentForm_4(forms.ModelForm):
    class Meta:
        model = Comment_4
        exclude = ('target', 'created_at')
       
