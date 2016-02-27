# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dappr', '0002_auto_20160207_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrationprofile',
            name='confirmation_key',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
    ]
