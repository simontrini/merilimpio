# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic
from .models import Post

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-creado_on')
    template_name = 'listaDePost.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'detalleDePost.html'
