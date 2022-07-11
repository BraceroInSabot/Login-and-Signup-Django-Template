from django.urls import path
from .views import SignUpView

urlpatterns = [
    path("/auth/signup", SignUpView.as_view(template_name="signup.html"), name="sign"),
]