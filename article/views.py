from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
)
from .serializers import (
    ArticleListSerializer,
    ArticleDetailSerializer,
    ArticleCreateSerializer
)
from .models import Article


class ArticleCreateAPIView(CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleCreateSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, last_modified_by=self.request.user)


class ArticleListAPIView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer


class ArticleDetailAPIView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer


class ArticleUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleCreateSerializer

    def perform_update(self, serializer):
        serializer.save(last_modified_by=self.request.user)


class ArticleDeleteAPIView(RetrieveDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
