from .views import UserCreateAPIView, UserLoginAPIView
from django.conf.urls import url


urlpatterns = [
    url(r'^register', UserCreateAPIView.as_view(), name="user_register"),
    url(r'^login', UserLoginAPIView.as_view(), name="user_login"),
]
