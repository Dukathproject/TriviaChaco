# from django.http import HttpResponse
# from django.template import Template, Context
from django.shortcuts import render, redirect
from MySQLdb import _mysql
from Trivia.forms import RegisterForm, LoginForm
from .db import register_post, user_login



def index(request):
    return render(request, "index.html")

#registrar usuario
def register(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        #funcion de para consultar usuario y registrar si no existe en db.py
        register_post(request)
    # if a GET (or any other method) we'll create a blank form
    form = RegisterForm()
    return render(request, "register.html", {'form': form})


def login(request):
    if request.method == 'POST':
        user_login(request)
    form = LoginForm()
    return render(request, "login.html")

def us(request):
    return render(request, "us.html")

# 