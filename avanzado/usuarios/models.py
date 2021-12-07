from django.db import models


class Usuario(models.Model):
    id = models.IntegerField(primary_key=True)
    year_birth = models.IntegerField()
    education = models.CharField(max_length=20)
    income = models.IntegerField()
