# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dappr', '0006_auto_20160222_0122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrationprofile',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
