from django import forms
from .models import NewsComment


class CommentForm(forms.ModelForm):
    class Meta:
        model = NewsComment
        fields = ('author', 'text')
