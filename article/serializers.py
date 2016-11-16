from rest_framework.serializers import ModelSerializer
from .models import Article
from account.serializers import UserDetailSerializer


class ArticleCreateSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'title',
            'content',
        ]


class ArticleListSerializer(ModelSerializer):
    created_by = UserDetailSerializer(read_only=True)

    class Meta:
        model = Article
        fields = [
            'id',
            'title',
            'content',
            'created_by',
            'image',
        ]


class ArticleDetailSerializer(ModelSerializer):
    created_by = UserDetailSerializer(read_only=True)

    class Meta:
        model = Article
        fields = [
            'id',
            'title',
            'content',
            'created_by',
            'image',
        ]