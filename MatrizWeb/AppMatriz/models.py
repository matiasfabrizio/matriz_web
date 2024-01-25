from django.db import models

class Curso(models.Model):

    nombre = models.CharField(max_length=40)


class Profesor(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)

