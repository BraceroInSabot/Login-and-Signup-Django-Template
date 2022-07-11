from django.shortcuts import render

# Forms
from django.urls import reverse_lazy
from core.forms import UserRegisterForm
from django.views.generic.edit import CreateView
from django.views import generic
from django.contrib.auth.forms import UserCreationForm

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("sign")


def index(request):
    return render(request, "index.html")
