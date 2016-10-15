from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now=False, auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    last_modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    last_modified_by = models.ForeignKey(User, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=0)
    date_published = models.DateTimeField(blank=True, null=True)
    ordering = models.IntegerField(default=1)

    def __str__(self):
        return self.title
