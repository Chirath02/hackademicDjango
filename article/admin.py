from django.contrib import admin

from .models import Articles
from .forms import ArticleForm




admin.site.register(Articles)