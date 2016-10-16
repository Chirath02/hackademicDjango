from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Class(models.Model):
    name = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
    archive = models.BooleanField(default=False)

    def __str__(self):
        return self.name
