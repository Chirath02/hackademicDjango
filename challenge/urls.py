from .views import ChallengeListAPIView
from django.conf.urls import url

urlpatterns = [
    url(r'^$', ChallengeListAPIView.as_view(), name='articles_list'),
]