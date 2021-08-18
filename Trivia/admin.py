from django.contrib import admin
from .models import Config_Partida, Pregunta, Respuesta, Eleccion_del_Usuario


# Register your models here.
admin.site.register(Config_Partida)
admin.site.register(Pregunta)
admin.site.register(Respuesta)
admin.site.register(Eleccion_del_Usuario)