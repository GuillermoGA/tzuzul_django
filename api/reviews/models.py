from django.db import models

# Create your models here.


class Review(models.Model):
    titulo = models.CharField(max_length=100)
    comentario = models.TextField()
    fecha = models.DateField()
