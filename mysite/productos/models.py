# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import User


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
TIPO = (
    (0,"Desinfectante"),
    (1,"Cloro"),
    (2,"Jabon"),
    (3,"Perfumen")
)
class Producto(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    codigo = models.CharField(max_length=100, unique=True)
    precio = models.FloatField()
    oferta = models.BooleanField(default=False)
    tipo = models.IntegerField(choices=TIPO, default=0)
    subido_on = models.DateTimeField(auto_now= True)
    contenido = models.TextField()
    creado_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField(upload_to="productos", null=True, blank=True,
        verbose_name="Imagen")

    class Meta:
        ordering = ['-creado_on']

    def __str__(self):
        return self.nombre