# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import User


STATUS = (
    (0,"Editando"),
    (1,"Publicado")
)
TIPO = (
    (0,"Normal"),
    (1,"VIP")
)
RED = (
    (0,"Facebook"),
    (1,"Imstagram"),
    (2,"twitter")
)
class Redes(models.Model):
    cuenta = models.CharField(max_length=200)
    tipo = models.IntegerField(choices=RED, default=0)
    def __str__(self):
        return "{}, {}".format(self.cuenta, RED[self.tipo])


class Cliente(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    redes = models.ManyToManyField(Redes, verbose_name="lista de redes")
    subido_on = models.DateTimeField(auto_now= True)
    contenido = models.TextField()
    creado_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    tipo = models.IntegerField(choices=TIPO, default=0)
    image = models.ImageField(upload_to="clientes", null=True, blank=True,
        verbose_name="Imagen")
    telefono = models.CharField(max_length=200)
    class Meta:
        ordering = ['-creado_on']

    def __str__(self):
        return self.nombre