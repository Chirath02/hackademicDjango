from django.db import models
from django.utils.translation import ugettext_lazy as _


class Challenge(models.Model):

    title = models.CharField(_('Title'), max_length=255)
    pkg_name = models.CharField(_('Package Name'), max_length=255)
    abstract = models.TextField(_('Abstract'))
    description = models.TextField(_('Description'))
    goal = models.TextField(_('Goal'))
    solution = models.TextField(_('Solution'))
    category = models.CharField(_('Category'), max_length=255)
    visibility = models.CharField(_('Visibility'), max_length=255)
    availability = models.CharField(_('Availability'), max_length=255)
    level = models.CharField(_('Level'), max_length=255)
    duration = models.IntegerField(_('Duration'), )
    default_points = models.IntegerField(_('Default Points'), )
    default_duration = models.IntegerField(_('Default Duration'), )

    date_posted = models.DateTimeField(_('Date Created'), auto_now_add=True, auto_now=False)
    created_by = models.ForeignKey('accounts.User', related_name='article_created_by', blank=True, null=True)
    date_modified = models.DateTimeField(_('Date Modified'), auto_now_add=False, auto_now=True, null=True)
    modified_by = models.ForeignKey('accounts.User', related_name='article_modified_by', blank=True, null=True)

    is_published = models.BooleanField(_('Published?'), default=False)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
