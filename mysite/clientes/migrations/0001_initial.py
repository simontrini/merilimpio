# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2020-03-24 23:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('subido_on', models.DateTimeField(auto_now=True)),
                ('contenido', models.TextField()),
                ('creado_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Editando'), (1, 'Publicado')], default=0)),
                ('tipo', models.IntegerField(choices=[(0, 'Normal'), (1, 'VIP')], default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='clientes', verbose_name='Imagen')),
                ('telefono', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['-creado_on'],
            },
        ),
        migrations.CreateModel(
            name='Redes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuenta', models.CharField(max_length=200)),
                ('tipo', models.IntegerField(choices=[(0, 'Facebook'), (1, 'Imstagram'), (2, 'twitter')], default=0)),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='redes',
            field=models.ManyToManyField(to='clientes.Redes', verbose_name='lista de redes'),
        ),
    ]
