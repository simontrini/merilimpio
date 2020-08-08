# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('titulo', 'slug', 'status','creado_on')
    list_filter = ("status",)
    search_fields = ['titulo', 'contenido']
    prepopulated_fields = {'slug': ('titulo',)}
    summernote_fields = ('contenido',)
