from django.contrib.auth import get_user_model
from django.db import models
from challenge.models import Challenge
from classes.models import Class

User = get_user_model()


class UserHasChallengeTocken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    token = models.CharField(max_length=300)

    def __str__(self):
        return "Tocken for " + self.user + " and " + self.challenge

class UserScore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    class_name = models.ForeignKey(Class)

    def __str__(self):
        return "Score for " + self.user
