from rest_framework.generics import ListAPIView
from .serializers import ArticleSerializer
from .models import Challenge


class ChallengeListAPIView(ListAPIView):
    queryset = Challenge.objects.all()
    serializer_class = ArticleSerializer

