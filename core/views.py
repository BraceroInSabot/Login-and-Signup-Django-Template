# Functions
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib.auth import authenticate, login as log_user
from django.contrib import messages

# Classes
from django.views.generic import TemplateView


class IndexView(TemplateView):
    pass


def signup(request):
    if request.method == "GET":
        return render(request, "signup.html")
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('c_password')

        if password != confirm_password:
            messages.add_message(request, constants.ERROR, "As suas senhas não batem!")
            return redirect('signup')

        if User.objects.filter(username=username).first():
            # messages.error(request, "Esse nome de usuário já está sendo usado!")
            messages.add_message(request, constants.ERROR, "Esse nome de usuário já está sendo usado!")
            return redirect('signup')
        elif User.objects.filter(email=email).first():
            messages.add_message(request, constants.ERROR, "Esse endereço de e-mail já existe!")
            return redirect('signup')

        create = User.objects.create_user(username=username, email=email, password=password, is_active=True,
                                          is_superuser=False, is_staff=False)
        create.save()

    messages.add_message(request, constants.SUCCESS, "PARABÉNS! Sua conta foi criada! Agora basta somente verificar o seu e-mail!")
    return render(request, "login.html")


def login_auth(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            log_user(request, user) # May a import error...
            messages.add_message(request, constants.SUCCESS, "Sucesso na autenticação!")
            return redirect('home')
        else:
            messages.add_message(request, constants.ERROR, "Houve um erro na autenticação! Tente novamente.")
            return redirect('login')

    else:
        return render(request, 'login.html')


