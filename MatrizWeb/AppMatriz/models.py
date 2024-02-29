from django.db import models

class Horario(models.Model):

    imagen = models.ImageField(upload_to='AppMatriz/assets/horario')

    def __str__(self) -> str:
        return f'Horario'