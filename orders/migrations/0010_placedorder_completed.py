# Generated by Django 2.0.3 on 2018-08-20 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_placedorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='placedorder',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]