from rest_framework import serializers
from accounts.models import User
from article.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        exclude = ('')
