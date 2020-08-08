# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#from django.shortcuts import render
from django.views import generic
from .models import Producto

class List(generic.ListView):
    model = Producto
    queryset = Producto.objects.filter(status=1).order_by('-creado_on')
    template_name = 'listaDeProductos.html'

class Detail(generic.DetailView):
    model = Producto
    template_name = 'detalleDeProducto.html'
