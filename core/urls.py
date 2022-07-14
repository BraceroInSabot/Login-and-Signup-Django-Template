from django.urls import path
from .views import IndexView

from core.views import signup

urlpatterns = [
    # Classes / POO
    path("", IndexView.as_view(template_name="index.html"), name="home"),

    # Functions
    path("signup", signup, name="signup"),
]