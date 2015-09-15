# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oca_test', '0005_auto_20150914_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='results',
            name='not_confident',
            field=models.BooleanField(default=False),
        ),
    ]
