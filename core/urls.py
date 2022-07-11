from django.urls import path
from .views import SignUpView

from core.views import index

urlpatterns = [
    # Classes / POO
    path("signup", SignUpView.as_view(template_name="signup.html"), name="sign"),

    # Functions
    path("", index, name="home"),
]