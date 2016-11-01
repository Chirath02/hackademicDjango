from rest_framework.serializers import ModelSerializer
from .models import Article


class ArticleListSerializer(ModelSerializer):

    class Meta:
        model = Article
        fields = [
            'id',
            'title',
            'content',
            'created_by',
        ]


class ArticleDetailSerializer(ModelSerializer):

    class Meta:
        model = Article
        fields = [
            'id',
            'title',
            'content',
            'created_by',
        ]