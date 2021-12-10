from django.db import models
from s3direct.fields import S3DirectField


class Usuario(models.Model):
    id = models.IntegerField(primary_key=True)
    year_birth = models.IntegerField()
    education = models.CharField(max_length=20)
    income = models.IntegerField()
    profile_pic = models.ImageField(upload_to="profile_pics", null=True)
    curriculum = S3DirectField(dest="primary_destination", blank=True )
    facturas = S3DirectField(dest="primary_destination", blank=True )
