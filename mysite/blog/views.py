# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic
from .models import Post
from productos.models import Producto

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-creado_on')
    template_name = 'listaDePost.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'detalleDePost.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['productos'] = Producto.objects.filter(status=1).order_by('-creado_on')
        return context