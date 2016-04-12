from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from article import views


urlpatterns = [
    url(r'article/$', views.ArtilceList.as_view()),
    url(r'article/(?P<pk>[0-9]+)/$', views.ArticleDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)