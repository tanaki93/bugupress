from django import forms
from .models import Opinion, OpinionComment


class AddForm(forms.ModelForm):
    class Meta:
        model = Opinion
        fields = ('title', 'body', 'keys',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = OpinionComment
        fields = ('author', 'text')
