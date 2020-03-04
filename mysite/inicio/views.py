# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
#from django.http import HttpResponse


def inicio(request):
    return render(request, 'inicio.html', {'poll': 'hola'})

def productos(request):
    return render(request, 'productos.html', {'poll': 'hola'})

def clientes(request):
    return render(request, 'clientes.html', {'poll': 'hola'})

def blog(request):
    return render(request, 'blog.html', {'poll': 'hola'})

def contacto(request):
    return render(request, 'contacto.html', {'poll': 'hola'})
