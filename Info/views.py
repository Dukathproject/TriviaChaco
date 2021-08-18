# from django.http import HttpResponse
# from django.template import Template, Context
from django.shortcuts import render, redirect
from MySQLdb import _mysql
from Trivia.forms import RegisterForm, LoginForm
from .db import register_post, user_login
from django.contrib.auth import logout



def index(request):
    return render(request, "index.html")

#registrar usuario
def register(request):
    if request.method == 'POST':
        register_post(request)  
        form = RegisterForm()
        return render(request, "register.html", {'form': form})
    else:
        form = RegisterForm()
        return render(request, "register.html", {'form': form})

#loguear usuario
def login(request):
    if request.method == 'POST':
        user_login(request)
        if request.user.is_authenticated:
            return render(request, "game.html")
        else:
            form = LoginForm()
            return render(request, "login.html", {'form': form, 'alert': 'El usuario y/o contraseña no corresponden a alguien registrado.'})        
    form = LoginForm()
    return render(request, "login.html", {'form': form})
    
    
    
def user_logout(request):
    logout(request)
    return render(request, "index.html")
    
    

def us(request):
    return render(request, "us.html")


def game(request):
    return render(request, "game.html")