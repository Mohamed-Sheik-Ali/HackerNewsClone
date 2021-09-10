from django import forms
from django.forms import fields
from .models import Post, Comment

# To create posts
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'url', )

# To create comments
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields=('body', )