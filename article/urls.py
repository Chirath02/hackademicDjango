from .views import ArticleListAPIView
from django.conf.urls import url

urlpatterns = [
    url(r'^$', ArticleListAPIView.as_view(), name='articles_list'),
]