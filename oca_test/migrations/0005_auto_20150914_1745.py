# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oca_test', '0004_auto_20150909_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='results',
            name='B_circle',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='results',
            name='E_circle',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.CharField(choices=[('1', '14-18'), ('2', '18+')], max_length=1, verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Адрес электронной почты', unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(choices=[('1', 'female'), ('2', 'male')], max_length=1, verbose_name='Пол'),
        ),
    ]
