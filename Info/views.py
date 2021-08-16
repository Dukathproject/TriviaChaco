# from django.http import HttpResponse
# from django.template import Template, Context
from django.shortcuts import render, redirect
from MySQLdb import _mysql
from Trivia.forms import RegisterForm
from .db import register_post


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
    return render(request, "login.html")

def us(request):
    return render(request, "us.html")

#-------------------------------------------------
# POSTS de formularios