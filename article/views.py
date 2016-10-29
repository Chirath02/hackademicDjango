from rest_framework.generics import ListAPIView
from .models import Article


class ArticleListAPIView(ListAPIView):
    queryset = Article.objects.all()
    
