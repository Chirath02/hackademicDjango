from django.contrib import admin
from .models import UserHasChallengeTocken, UserScore

admin.site.register(UserScore)
admin.site.register(UserHasChallengeTocken)