# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20170309_0733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Phone',
            field=models.IntegerField(default='', editable=False),
        ),
    ]
