from django.db import models

class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    horario = models.CharField(max_length=7)

class Profesor(models.Model):

    nombre = models.CharField(max_length=40)

