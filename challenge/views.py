from rest_framework.generics import ListAPIView
from .serializers import ArticleSerializer
from .models import Article


class ArticleListAPIView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

