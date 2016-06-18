from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from article import views


urlpatterns = [
    url(r'article/$',
        views.ArticleList.as_view(),
        name='article-list'),
    url(r'article/(?P<pk>[0-9]+)/$',
        views.ArticleDetail.as_view(),
        name='article-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)