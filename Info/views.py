# from django.http import HttpResponse
# from django.template import Template, Context
from django.shortcuts import render, redirect
from MySQLdb import _mysql
from Trivia.forms import RegisterForm, LoginForm, RankingForm, AvatarForm
from .db import register_post, user_login, questions, ranking_post, ranking_get, historial_get, own_historial_get, login_data_get, category_data_get, profile_get, profile_post
from django.contrib.auth import logout
from django.http import JsonResponse
import json


#INDEX-------------------------------------------------------------------------
def index(request):
    if request.user.is_authenticated:
        historial = own_historial_get(request)
        avatar = profile_get(request)
        return render(request, "lobby.html", {'historial': historial, 'avatar': avatar})
    else:
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
            historial = own_historial_get(request)
            avatar = profile_get(request)
            return render(request, "lobby.html", {'historial': historial, 'avatar': avatar})
        else:
            form = LoginForm()
            return render(request, "login.html", {'form': form, 'alert': 'El usuario y/o contraseña no corresponden a alguien registrado.'})        
    form = LoginForm()
    return render(request, "login.html", {'form': form})


#LOBBY-------------------------------------------------------------------------
def lobby(request):
    if request.user.is_authenticated:
        historial = own_historial_get(request)
        avatar = profile_get(request)
        return render(request, "lobby.html", {'historial': historial, 'avatar': avatar})
    else:
        return render(request, "index.html") 
  
  
#THE GAME-------------------------------------------------------------------   
def game(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            partida_id = ranking_post(request)
            return redirect('/' + str(partida_id) + '/')
        else:
            questions_list = json.dumps(questions())
            form = RankingForm()
            avatar = profile_get(request)
            return render(request, "game.html", {'question':questions_list, 'form': form, 'avatar': avatar})
    else:
        form = LoginForm()
        return render(request, "login.html", {'form': form, 'alert': 'Para jugar debe iniciar sesión.'})


#RANKING-------------------------------------------------------------------    
def ranking(request):
    rank = ranking_get()
    avatar = profile_get(request)
    return render(request, "ranking.html", {'rank': rank, 'avatar': avatar})


#LOG OUT-------------------------------------------------------------------    
def user_logout(request):
    logout(request)
    return render(request, "index.html")
    
    
#US----------------------------------------------------------------------------
def us(request):
    avatar = profile_get(request)
    print(avatar)
    return render(request, "us.html", {'avatar': avatar})


#HISTORIAL---------------------------------------------------------------------
def historial(request, partida_id):
    result = historial_get(partida_id)
    avatar = profile_get(request)
    return render(request, "result.html", {'result': result, 'avatar': avatar})

#DATA---------------------------------------------------------------------
def data(request):
    if request.user.is_authenticated:
        if request.user.id == 1:
            login_data = json.dumps(login_data_get())
            category_data = json.dumps(category_data_get())
            avatar = profile_get(request)
            return render(request, "data.html",{'login_data': login_data, 'category_data': category_data, 'avatar': avatar})
        else:
            msg = "Debe ser administrador para acceder."
            return render(request, "lobby.html", {'msg': msg})
    else:
        msg = "Debe iniciar sesión para acceder."
        return render(request, "index.html", {'msg': msg})
    
#PROFILE-----------------------------------------------------------------------
def profile(request):
    if request.method == 'POST':
        avatar = profile_post(request)
    form = AvatarForm()
    avatar = profile_get(request)
    return render(request, "profile.html", {'form': form,'avatar': avatar})
        