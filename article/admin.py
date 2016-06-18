from django.contrib import admin

from .models import Article
from .forms import ArticleForm




admin.site.register(Article)