from .views import ArticleListAPIView, ArticleDetailAPIView
from django.conf.urls import url, include
from rest_framework import routers

router = routers.DefaultRouter()
#router.register(r'a', ArticleListAPIView)
#router.register(r'^(?P<pk>\d+)/$', ArticleDetailAPIView)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^article', include(router.urls)),
]
