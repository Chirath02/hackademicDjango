from django import forms
from .models import Articles


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        exclude = []