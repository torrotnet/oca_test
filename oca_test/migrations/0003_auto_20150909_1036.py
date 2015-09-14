# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oca_test', '0002_question_character'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='number',
            field=models.IntegerField(unique=True),
        ),
    ]
