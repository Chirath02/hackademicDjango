from django.db.models import Q
from rest_framework.filters import SearchFilter, OrderingFilter
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
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny)
from .permissions import IsOwnerOrReadOnly
# permission to check whether the user is the owner of the post


class ArticleCreateAPIView(CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, last_modified_by=self.request.user)


class ArticleListAPIView(ListAPIView):
    """
    to search and order based on he search_fields
    /api/article/?search=<query>&?ordering=<item>
    """

    permission_classes = [AllowAny]
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer
    queryset_list = Article.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'content', 'created_by__username']


class ArticleDetailAPIView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
    permission_classes = [AllowAny]


class ArticleUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleCreateSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(last_modified_by=self.request.user)


class ArticleDeleteAPIView(RetrieveDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]
