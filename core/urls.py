from django.urls import path
from .views import SignUpView

from core.views import index

urlpatterns = [
    path("/auth/signup", SignUpView.as_view(template_name="signup.html"), name="sign"),
    path("", index, name="home"),
]