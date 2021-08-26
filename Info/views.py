# from django.http import HttpResponse
# from django.template import Template, Context
from django.shortcuts import render, redirect
from MySQLdb import _mysql
from Trivia.forms import RegisterForm, LoginForm, RankingForm
from .db import register_post, user_login, questions, ranking_post
from django.contrib.auth import logout
import json


#INDEX-------------------------------------------------------------------------
def index(request):
    return render(request, "index.html")


#REGISTER USER-----------------------------------------------------------------
def register(request):
    if request.method == 'POST':
        msg = register_post(request) 
        if msg[0]:     
            #si el usuario no existe, lo crea y redirige al index con mensaje de exito.
            return render(request, "index.html", {'msg': msg[1]})
        else:
            #si el usuario ya existe redirige al register con mensaje de usuario existente.
            form = RegisterForm()
            return render(request, "register.html", {'form': form, 'msg': msg[1]})
    form = RegisterForm()
    return render(request, "register.html", {'form': form})


#LOG IN------------------------------------------------------------------------
def login(request):
    if request.method == 'POST':
        user_login(request)
        if request.user.is_authenticated:
            return render(request, "lobby.html")
        else:
            form = LoginForm()
            return render(request, "login.html", {'form': form, 'alert': 'El usuario y/o contraseña no corresponden a alguien registrado.'})        
    form = LoginForm()
    return render(request, "login.html", {'form': form})


#LOBBY-------------------------------------------------------------------------
def lobby(request):
    if request.user.is_authenticated:
        return render(request, "lobby.html")
    else:
        return render(request, "index.html") 
  
  
#THE GAME-------------------------------------------------------------------   
def game(request):
    if request.method == 'POST':
        result = ranking_post(request)
        if request.user.is_authenticated:
            return render(request, "result.html", {'result': result})
    if request.user.is_authenticated:
        questions_list = json.dumps(questions())
        form = RankingForm()
        return render(request, "game.html", {'question':questions_list, 'form': form})
    else:
        form = LoginForm()
        return render(request, "login.html", {'form': form, 'alert': 'Para jugar debe iniciar sesión.'})


#LOG OUT-------------------------------------------------------------------    
def user_logout(request):
    logout(request)
    return render(request, "index.html")
    
    
#US----------------------------------------------------------------------------
def us(request):
    return render(request, "us.html")