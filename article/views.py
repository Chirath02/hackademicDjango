from article.models import Article
from article.serializers import ArticleSerializer
from rest_framework import generics


class ArticleList(generics.ListCreateAPIView):
    '''
    List all articles or create a new article using generic LIstCreateApiView
    '''
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Retrieve, update or delete an article instance
    '''
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
