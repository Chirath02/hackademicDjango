from django.shortcuts import render
from django.contrib.auth.forms import PasswordResetForm
from django.shortcuts import redirect
from django.views.generic import CreateView

from .forms import RegistrationForm
from .models import User


def register(request):
    form = RegistrationForm()
    context = {
        "form":form
    }
    return render(request, "signup.html", context)