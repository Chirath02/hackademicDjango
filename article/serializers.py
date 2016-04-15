from rest_framework import serializers
from accounts.models import User
from article.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    modified_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Article
        exclude = ('')
