# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20170309_0830'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='Phone',
        ),
    ]
