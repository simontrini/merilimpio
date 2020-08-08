# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Cliente, Redes

@admin.register(Cliente)
class ClienteAdmin(SummernoteModelAdmin):
    list_display = ('nombre', 'slug', 'status','creado_on')
    list_filter = ("status",)
    search_fields = ['nombre', 'contenido']
    prepopulated_fields = {'slug': ('nombre',)}
    summernote_fields = ('contenido',)


@admin.register(Redes)
class RedesAdmin(admin.ModelAdmin):
    list_display = ('cuenta', 'tipo')
    list_filter = ("tipo",)
    search_fields = ['cuenta', 'tipo']
