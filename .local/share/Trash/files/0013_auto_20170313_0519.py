# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_auto_20170313_0508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='stud_id',
            field=models.AutoField(default='', serialize=False, primary_key=True),
        ),
    ]
