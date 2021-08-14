# from django.http import HttpResponse
# from django.template import Template, Context
from django.shortcuts import render, redirect
import os
import sys


#agregar redirect para las rutas erroneas



def index(request):
    return render(request, "index.html")

def register(request):
    return render(request, "register.html")

def login(request):
    #if url == "login" and method == "post"
        #revisar usuario y contraseña
    return render(request, "login.html")




# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# def home(request):
#     saludo_view = open(os.path.join(os.path.dirname(BASE_DIR + "/info/views/"), "index.html"))
#     plantilla_saludo = Template(saludo_view.read())
#     saludo_view.close()
#     contexto = Context()
#     saludo = plantilla_saludo.render(contexto)
#     return HttpResponse(saludo)

# def login(request):
#     saludo_view = open(os.path.join(os.path.dirname(BASE_DIR + "/info/views/"), "login.html"))
#     plantilla_saludo = Template(saludo_view.read())
#     saludo_view.close()
#     contexto = Context()
#     saludo = plantilla_saludo.render(contexto)
#     return HttpResponse(saludo)

# def register(request):
#     saludo_view = open(os.path.join(os.path.dirname(BASE_DIR + "/info/views/"), "register.html"))
#     plantilla_saludo = Template(saludo_view.read())
#     saludo_view.close()
#     contexto = Context()
#     saludo = plantilla_saludo.render(contexto)
#     return HttpResponse(saludo)