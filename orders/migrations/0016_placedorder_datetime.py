# Generated by Django 2.0.3 on 2018-08-20 12:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0015_auto_20180820_1153'),
    ]

    operations = [
        migrations.AddField(
            model_name='placedorder',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 20, 11, 59, 19, 963465)),
        ),
    ]