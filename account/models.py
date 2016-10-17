from django.db import models
from django.contrib.auth.models import User
from challenge.models import Challenge


class UserHasChallengeTocken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    token = models.CharField(max_length=300)

    def __str__(self):
        return "Tocken for " + self.user + " and " + self.challenge