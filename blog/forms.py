from django import forms

from .models import Post


# TODO: удалить неиспользуюмую форму

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
