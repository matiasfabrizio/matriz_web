from django.db import models

class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    horario = models.CharField(max_length=17)
    codigo = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.nombre} - Horario: {self.horario} - Código: {self.codigo}"

class Profesor(models.Model):

    nombre = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.nombre}"
