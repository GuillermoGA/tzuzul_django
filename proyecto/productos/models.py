from django.db import models


# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    cantidad = models.IntegerField(default=0)
    precio = models.FloatField()
    descripcion = models.TextField(null=True)

    def __str__(self):
        return f"id:{self.id} ({self.cantidad}) {self.nombre} {self.precio}$"
