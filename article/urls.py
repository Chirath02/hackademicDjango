from .views import (
    ArticleListAPIView,
    ArticleDetailAPIView,
    ArticleUpdateAPIView,
    ArticleDeleteAPIView
)
from django.conf.urls import url

urlpatterns = [
    url(r'^$', ArticleListAPIView.as_view(), name='articles_list'),
    url(r'^(?P<pk>\d+)/$', ArticleDetailAPIView.as_view(), name='article_detail'),
    url(r'^(?P<pk>\d+)/update', ArticleUpdateAPIView.as_view(), name='article_update'),
    url(r'^(?P<pk>\d+)/delete', ArticleDeleteAPIView.as_view(), name='article_delete')
]