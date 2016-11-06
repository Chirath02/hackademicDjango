from .views import UserCreateAPIView
from django.conf.urls import url


urlpatterns = [
    url(r'^create', UserCreateAPIView.as_view(), name="create_user")
]
