# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oca_test', '0006_results_not_confident'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(default='2', choices=[('1', 'Женский'), ('2', 'Мужской')], max_length=1, verbose_name='Пол'),
        ),
    ]
