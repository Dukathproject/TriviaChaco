from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200,blank=True)
    
class Question(models.Model):
    question = models.CharField(max_length=200, null=False)
    difficulty = models.IntegerField(null=False, default=1)
    
class Ranking(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    level = models.IntegerField(null=False, default=0)