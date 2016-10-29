from rest_framework.serializers import ModelSerializer
from .models import Challenge


class ArticleSerializer(ModelSerializer):

    class Meta:
        model = Challenge
        fields = [
            'id',
            'title',
            'description',
            'authors',
        ]