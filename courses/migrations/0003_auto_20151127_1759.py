# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20151126_1804'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='courses',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
