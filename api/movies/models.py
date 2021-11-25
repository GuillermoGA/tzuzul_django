from django.db import models

# Create your models here.


class Movie(models.Model):
    titulo = models.CharField(max_length=100)
    fecha_publicacion = models.DateField()
    director = models.CharField(max_length=120)
