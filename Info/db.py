from MySQLdb import _mysql
from Trivia.forms import RegisterForm

#conectar a la base de datos
db=_mysql.connect(host="127.0.0.1",user="root", passwd="dukath1234",db="informatorio", port=3306)

#funcion para consultar si existe usuario en db, si no existe lo agrega
def register_post(request):
    # create a form instance and populate it with data from the request:
    form = RegisterForm(request.POST)
    # check whether it's valid:
    if form.is_valid():
        # process the data in form.cleaned_data as required
        form_data = form.cleaned_data
        #revisar en db si ya existe usuario
        query_str = f"""SELECT name FROM informatorio.trivia_user
                    WHERE name = '{form_data['name']}';""" 
        db.query(query_str)
        r=db.store_result()
        query_result = r.fetch_row(maxrows=1)
        if query_result:
            print("usuario ya existente")
            #redireccionar
        else:
            #si no existe usuario, se crea
            print("usuario creado")
            query_str = f"""INSERT INTO `informatorio`.`trivia_user` (`name`, `email`, `password`) VALUES ('{form_data['name']}', '{form_data['email']}','{form_data['password']}');"""
            db.query(query_str)
            