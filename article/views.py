from article.models import Article
from article.serializers import ArticleSerializer
from rest_framework import generics
from rest_framework import permissions


class ArticleList(generics.ListCreateAPIView):
    '''
    List all articles or create a new article using generic LIstCreateApiView
    '''
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Retrieve, update or delete an article instance
    '''
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
