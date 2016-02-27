# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dappr', '0003_auto_20160213_0010'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrationprofile',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
