from django.contrib import admin
from .models import Config_Partida, Pregunta, Respuesta, Ranking


# Register your models here.
admin.site.register(Config_Partida)
admin.site.register(Pregunta)
admin.site.register(Respuesta)
admin.site.register(Ranking)