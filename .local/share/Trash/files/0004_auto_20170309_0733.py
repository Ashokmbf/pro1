# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20170309_0624'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='address',
            new_name='Address',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='first_name',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='last_name',
            new_name='Sur_Name',
        ),
        migrations.AddField(
            model_name='student',
            name='Name',
            field=models.CharField(default='', max_length=50, editable=False),
        ),
        migrations.AddField(
            model_name='student',
            name='Phone',
            field=models.IntegerField(default='', max_length=50, editable=False),
        ),
    ]
