# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0067_auto_20160910_0836'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fundingcommitment',
            name='intervention',
        ),
    ]
