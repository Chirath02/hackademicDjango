from django.db import models
from django.contrib.auth.models import User

class Class(models.Model):
    name = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
    archive = models.BooleanField(default=False)
    user = models.ForeignKey(User, related_name="User")

    def __str__(self):
        return self.name

class ClassChallenge(models.Model):
    challenge_id = models.IntegerField()
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE, related_name="Class")
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.challenge + " of " + self.class_name