from rest_framework.serializers import ModelSerializer
from .models import Challenge


class ChallengeListSerializer(ModelSerializer):

    class Meta:
        model = Challenge
        fields = [
            'id',
            'title',
            'description',
            'authors',
        ]


class ChallengeDetailSerializer(ModelSerializer):

    class Meta:
        model = Challenge
        fields = [
            'id',
            'title',
            'description',
            'authors',
        ]