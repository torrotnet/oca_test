# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oca_test', '0007_auto_20150915_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.CharField(max_length=1, choices=[('1', '14-18'), ('2', '18+')], default='2', verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(max_length=1, choices=[('1', 'Женский'), ('2', 'Мужской')], verbose_name='Пол'),
        ),
    ]
