# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_auto_20170310_1140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.AddField(
            model_name='student',
            name='stud_id',
            field=models.AutoField(default='1', serialize=False, primary_key=True),
        ),
    ]
