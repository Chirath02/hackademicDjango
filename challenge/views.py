from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import ChallengeListSerializer, ChallengeDetailSerializer
from .models import Challenge


class ChallengeListAPIView(ListAPIView):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeListSerializer


class ChallengeDetailAPIView(RetrieveAPIView):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeListSerializer

