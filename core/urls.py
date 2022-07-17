from django.urls import path, include
from .views import IndexView, PageView

from core.views import signup, login_auth

urlpatterns = [
    # Classes / POO
    path("", IndexView.as_view(template_name="index.html"), name="home"),
    path("page/", PageView.as_view(template_name="page.html"), name="page"),

    # Functions
    path("signup/", signup, name="signup"),
    path("login/", login_auth, name="login"),
]