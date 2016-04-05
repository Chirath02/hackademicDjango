from django.contrib import admin

from .models import Articles
from .forms import ArticleForm


class ArticleAdmin(admin.ModelAdmin):
    form = ArticleForm

admin.site.register(Articles, ArticleForm)