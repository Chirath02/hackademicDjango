from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, email, username, password, **kwargs):
        """
        Creates and saves a User with the given email, email and password.
        """
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password, **kwargs):
        """
        Creates and saves a superuser with the given email, username and password.
        """
        user = self.model(
            email=email,
            username=username,
            is_admin=True,
            is_active=True,
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    Extends the default User profiles of Django. The fields of this model can be obtained by the
    user.get_profile method and it's extended by the django-profile application.
    """

    email = models.EmailField(unique=True)
    full_name = models.CharField(_('User Name'), max_length=50, unique=True, blank=True, null=True)
    user_pic = models.ImageField(_('Photo'), upload_to='user_pic', blank=True, null=True)
    username = models.CharField(_('User Name'), max_length=50, unique=True, blank=True, null=True,
                                    validators=[RegexValidator(regex='^[A-Za-z]*$')])

    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)

    token = models.IntegerField(default=0)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.email

    def __unicode__(self):
        return self.username

    def __str__(self):
        return self.username
