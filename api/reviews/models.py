from django.db import models
from movies.models import Movie

# Create your models here.


class Review(models.Model):
    titulo = models.CharField(max_length=100)
    comentario = models.TextField()
    fecha = models.DateField()
    estrellas = models.IntegerField()

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True)