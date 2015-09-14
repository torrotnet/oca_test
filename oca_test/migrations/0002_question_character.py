# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oca_test', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='character',
            field=models.CharField(default='A', max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J')]),
        ),
    ]
