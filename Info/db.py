from MySQLdb import _mysql
from Trivia.forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.db import models
from Trivia.models import Config_Partida, Pregunta, Respuesta, Ranking
import random

#----------------------------------
#Consultas del juego
def questions():
    #consulta todas las preguntas
    p = Pregunta.objects.all().values()
    r = Respuesta.objects.all().values()
    c = Config_Partida.objects.all().values()
    # r = Respuesta.objects.all().filter(pregunta_id=21)['respuesta']
    questions_list = {}
    for i in range(5):
        #numero al azar segun cantidad de preguntas totales
        randNum = random.randint(0,len(p)-1)
        #de las preguntas consultadas, se toman 5 al azar y se guarda 
        questions_list['question_' + str(i+1)] = {
            'id': p[randNum]['id'],
            'formula': p[randNum]['formula'],
            'categoría': c[p[randNum]['trivia_id']-1]['nombre']
            }
        #según las preguntas al azar tomadas se filtran las respectivas respuestas y se agregan a questions_list
        resp_cont = 0
        for respuesta in r:
            #HAY ERROR CUANDO SALE ID TOTAL DE LA DB, GESTIONAR EL NUMERO MAXIMO
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
        try:
            check = User.objects.get(username=form_data['name'])
        except:
            user = User.objects.create_user(form_data['name'], form_data['email'], form_data['password'])
            msg = [True, "Usuario creado de forma exitosa!"]
            return msg
        msg = [False, "Usuario ya existente, ingrese otro nombre de usuario."]
        return msg
            
            
 
 
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