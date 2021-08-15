# from django.http import HttpResponse
# from django.template import Template, Context
from django.shortcuts import render, redirect
from MySQLdb import _mysql
from Trivia.forms import RegisterForm

#conectar a la base de datos
db=_mysql.connect(host="127.0.0.1",user="root", passwd="dukath1234",db="informatorio", port=3306)


#----------------------------------------------------------------------
#insertar en db
# db.query("""INSERT INTO `informatorio`.`trivia_user` (`name`, `email`, `password`) VALUES ('test2', 'test2@gmail.com', 'pass123445');""")

#consulta en db
db.query("""SELECT * FROM informatorio.trivia_user;""")
r=db.store_result()
query_result = r.fetch_row(maxrows=0, how=1)

#mostrar consulta
for consulta in query_result:
    print(consulta["id"])
print(query_result[0]["name"])
# db.query("""INSERT trivia_user
# 	values ('Test', 'dukath@gmail.com', 'pass1234');""")
#----------------------------------------------------------------------

#agregar redirect para las rutas erroneas
def index(request):
    return render(request, "index.html")

#registracion
def register(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            print(form.cleaned_data)
            # redirect to a new URL:
            # return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegisterForm()
    return render(request, "register.html", {'form': form})



def login(request):
    return render(request, "login.html")

#-------------------------------------------------
# POSTS de formularios