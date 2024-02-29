from django.db import models

class Horario(models.Model):

    nombre = models.CharField(max_length=40, default='no_name')
    imagen = models.ImageField(upload_to='AppMatriz/assets/horario')

    def __str__(self) -> str:
        return f'Nombre: {self.nombre}'