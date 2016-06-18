from django.db import models
from django.utils.translation import ugettext_lazy as _


class Article(models.Model):

    title = models.CharField(_('Title'), max_length=255)
    content = models.TextField(_('Contents'))

    date_added = models.DateTimeField(_('Date Created'), auto_now_add=True, auto_now=False)
    created_by = models.ForeignKey('accounts.User', related_name='article_created_by', blank=True, null=True)
    date_modified = models.DateTimeField(_('Date Modified'), auto_now_add=False, auto_now=True, null=True)
    modified_by = models.ForeignKey('accounts.User', related_name='article_modified_by', blank=True, null=True)
    ordering = models.IntegerField(_('Ordering'), )
    is_published = models.BooleanField(_('Published?'), default=False)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title