from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class Classes(models.Model):

    classname = models.CharField(_('Class Name'), max_length=200)

    is_archived = models.BooleanField(default=False)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

    # created_by = models.ForeignKey('accounts.User')
    # modified_by = models.ForeignKey('accounts.User')

    def __unicode__(self):
        return self.classname

    def __str__(self):
        return self.classname
