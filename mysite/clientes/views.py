# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic
from .models import Cliente

class List(generic.ListView):
    model = Cliente
    queryset = Cliente.objects.filter(status=1).order_by('-creado_on')
    template_name = 'lista.html'

class Detail(generic.DetailView):
    model = Cliente
    template_name = 'detalle.html'

