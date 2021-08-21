from MySQLdb import _mysql
from Trivia.forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.db import models
from Trivia.models import Config_Partida, Pregunta, Respuesta, Eleccion_del_Usuario
import random

#----------------------------------
#Consultas del juego
def questions():
    #consulta todas las preguntas
    p = Pregunta.objects.all().values()
    r = Respuesta.objects.all().values()
    # r = Respuesta.objects.all().filter(pregunta_id=21)['respuesta']
    questions_list = {}
    for i in range(5):
        #numero al azar segun cantidad de preguntas totales
        randNum = random.randint(0,len(p))
        #de las preguntas consultadas, se toman 5 al azar y se guarda 
        questions_list['question_' + str(i+1)] = {
            'id': p[randNum]['id'],
            'formula': p[randNum]['formula']
            }
        #según las preguntas al azar tomadas se filtran las respectivas respuestas y se agregan a questions_list
        resp_cont = 0
        for respuesta in r:
            if respuesta['pregunta_id'] == randNum+1:
                resp_cont = resp_cont + 1
                questions_list['question_' + str(i+1)]['respuesta_' + str(resp_cont)] = {
                    'formula': respuesta['formula'],
                    'correcta': respuesta['correcta']
                }
    return questions_list




#funcion para consultar si existe usuario en db, si no existe lo agrega
def register_post(request):
    # create a form instance and populate it with data from the request:
    form = RegisterForm(request.POST)
    # check whether it's valid:
    if form.is_valid():
        form_data = form.cleaned_data
        user = User.objects.create_user(form_data['name'], form_data['email'], form_data['password'])
 
 
def user_login(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        form_data = form.cleaned_data
        user = authenticate(request, username=form_data['name'], password=form_data['password'])
        if user is not None:
            login(request, user)
            # A backend authenticated the credentials
        # else:
            # No backend authenticated the credentials
    
    

        # process the data in form.cleaned_data as required
        # form_data = form.cleaned_data
        # #revisar en db si ya existe usuario
        # query_str = f"""SELECT name FROM informatorio.trivia_user
        #             WHERE name = '{form_data['name']}';""" 
        # db.query(query_str)
        # r=db.store_result()
        # query_result = r.fetch_row(maxrows=1)
        # if query_result:
        #     print("usuario ya existente")
        #     #redireccionar
        # else:
        #     #si no existe usuario, se crea
        #     print("usuario creado")
        #     query_str = f"""INSERT INTO `informatorio`.`trivia_user` #(`name`, `email`, `password`) VALUES ('{form_data['name']}', '{form_data['email']}','{form_data['password']}');"""
        #     db.query(query_str)