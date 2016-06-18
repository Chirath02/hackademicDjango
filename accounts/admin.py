from django.contrib import admin

from .models import User
from .forms import RegistrationForm


class UserRegistrastionAdmin(admin.ModelAdmin):
    form = RegistrationForm

admin.site.register(User, UserRegistrastionAdmin)