from django.db import models
from django.contrib.auth.models import User

class Challenge(models.Model):
    title = models.CharField(max_length=300)
    pkg_name = models.CharField(max_length=100)
    description = models.TextField()
    authors = models.ManyToManyField(User, related_name="authors")
    category = models.CharField(max_length=200)
    date_posted = models.DateTimeField(auto_now=False, auto_now_add=True)
    visibility = models.CharField(default='private', max_length=100)
    is_published = models.BooleanField(default=0)
    abstract = models.CharField(max_length=500, default="")
    ordering = models.IntegerField(default=1)
    level = models.CharField(max_length=300, default="")
    duration = models.TimeField(blank=True, null=True, )
    goal = models.CharField(max_length=300, default="")
    solution = models.CharField(max_length=300, default="")
    availability = models.CharField(max_length=100, default='private')
    default_points = models.IntegerField()
    default_duration = models.TimeField(blank=True, null=True)

    image = models.ImageField(blank=True, null=True, upload_to='challenges/')

    def __str__(self):
        return self.title
