# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_remove_student_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='Address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Email',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Sur_Name',
            new_name='last_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='Name',
        ),
    ]
