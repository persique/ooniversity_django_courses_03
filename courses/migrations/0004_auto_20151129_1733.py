# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0001_initial'),
        ('courses', '0003_auto_20151128_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='assistant',
            field=models.ForeignKey(related_name=b'assistant_courses', blank=True, to='coaches.Coach', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='coach',
            field=models.ForeignKey(related_name=b'coach_courses', blank=True, to='coaches.Coach', null=True),
            preserve_default=True,
        ),
    ]
