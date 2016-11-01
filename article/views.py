from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import ArticleListSerializer, ArticleDetailSerializer
from .models import Article


class ArticleListAPIView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer


class ArticleDetailAPIView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer

