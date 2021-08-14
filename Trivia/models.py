from django.db import models

# Create your models here.

class Cliente(models.Model):
    
    user = models.CharField(max_length=200)
    password = models.CharField(max_length=200,blank=True)