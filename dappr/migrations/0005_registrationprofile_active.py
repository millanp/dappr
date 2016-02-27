# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dappr', '0004_registrationprofile_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrationprofile',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
