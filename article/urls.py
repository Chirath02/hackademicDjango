from .views import ArticleListAPIView, ArticleDetailAPIView
from django.conf.urls import url

urlpatterns = [
    url(r'^$', ArticleListAPIView.as_view(), name='articles_list'),
    url(r'^(?P<pk>\d+)/$', ArticleListAPIView.as_view(), name='article_detail'),
]