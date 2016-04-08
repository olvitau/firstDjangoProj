# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-06 15:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('article text', models.TextField(verbose_name='Текст')),
                ('article date', models.DateTimeField(verbose_name='Дата добавления')),
                ('article author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'ordering': ('article date',),
                'verbose_name_plural': 'Статьи',
                'db_table': 'articles',
                'verbose_name': 'Статья',
            },
        ),
    ]