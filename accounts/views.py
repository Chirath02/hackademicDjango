from accounts.models import User
from accounts.serializers import UserSerializer
from article.models import Article
from article.serializers import ArticleSerializer
from rest_framework import generics
from rest_framework import permissions


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
