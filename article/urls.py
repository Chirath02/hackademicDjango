from django.conf.urls import url
from article import views


urlpatterns = [
    url(r'article/$', views.artilce_list),
    url(r'article/(?P<pk>[0-9]+)/$', views.article_detail),
]
