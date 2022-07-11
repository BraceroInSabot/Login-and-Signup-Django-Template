from django.db import models

# Create your models here.

# Register
class RegisterForm(models.Model):
    name = models.CharField("Name", max_length=30, help_text="Insert your name")
    email = models.EmailField("Email", max_length=60, help_text="Insert your email")
    # password = models.CharField("Password", max_length=20, widget=models.PasswordInput(), help_text="Insert your password")
    confirm = models.CharField("Confirm your password", max_length=20)
