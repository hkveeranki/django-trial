# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-12 21:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=80)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
