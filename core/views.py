# Functions
from django.shortcuts import render

# Classes
from django.views.generic import TemplateView, ListView


class IndexView(TemplateView):
    pass


def signup(request):
    return render(request, "signup.html")
