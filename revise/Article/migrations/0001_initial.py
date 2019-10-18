# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-08-07 17:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField(max_length=500)),
                ('adate', models.DateTimeField(auto_now_add=True)),
                ('author', models.CharField(max_length=100)),
            ],
        ),
    ]
