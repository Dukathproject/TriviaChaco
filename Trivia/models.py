from django.db import models
from django.contrib.auth.models import User
import random

class Config_Partida(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)    
    numero_de_preguntas = models.IntegerField(default=1)
    tiempo = models.IntegerField(help_text="Duración de la trivia en segundos", default="1")
    
    def __str__(self):
        return self.nombre
    
    def get_preguntas(self):
        return self.preguntas_set.all()
    
class Pregunta(models.Model):
    formula = models.CharField(max_length=200)
    trivia = models.ForeignKey(Config_Partida, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.formula
    
    def get_respuestas(self):
        return self.respuestas_set.all()
    
    
class Respuesta(models.Model):
    formula = models.CharField(max_length=200)
    correcta = models.BooleanField(default=False)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Pregunta: {self.pregunta.formula}, answer: {self.formula}, correct: {self.correcta}"
    
class Eleccion_del_Usuario(models.Model):
    trivia = models.ForeignKey(Config_Partida, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    aciertos = models.FloatField()
    
    def __str__(self):
        return str(self.trivia)