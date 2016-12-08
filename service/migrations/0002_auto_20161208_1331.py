# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Apple_models',
            new_name='Apple_model',
        ),
        migrations.RenameModel(
            old_name='Type_of_parts',
            new_name='Type_of_part',
        ),
    ]
