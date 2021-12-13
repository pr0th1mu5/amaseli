from django.db import models
from django.db.models.base import Model
from django.shortcuts import render

# Create your models here.
class Noticias(models.Model):
    tituloNoticia = models.CharField(max_length=200)
    corpoNoticia = models.TextField()
    dataNoticia = models.DateField()

    def __str__(self):
        return self.tituloNoticia