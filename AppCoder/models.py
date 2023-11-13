# La estructura que se le da a un dato

from django.db import models

# Create your models here.


class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()


class Student(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

