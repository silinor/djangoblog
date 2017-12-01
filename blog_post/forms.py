from django.forms import ModelForm
from .models import Post, Comment


class PostAddForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']


class CommentAddForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment', 'post', 'user']
