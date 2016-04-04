from django.db import models
from django.utils.translation import ugettext_lazy as _


class Articles(models.Model):

    title = models.CharField(_('Title'), max_length=255)
    content = models.TextField()

    date_added = models.DateTimeField(auto_now_add=True, auto_now=False)
    created_by = models.ForeignKey('accounts.User')
    date_modified = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)
    modified_by = models.ForeignKey('accounts.User')
    ordering = models.IntegerField()
    is_published = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title