# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(SummernoteModelAdmin):
    list_display = ('nombre','status','creado_on')
    list_filter = ("status",)
    search_fields = ['nombre', 'contenido']
    summernote_fields = ('contenido',)
