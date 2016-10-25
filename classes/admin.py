from django.contrib import admin
from .models import Class, ClassChallenge, ClassMembership

# Register your models here.

admin.site.register(Class)
admin.site.register(ClassMembership)
admin.site.register(ClassChallenge)