# Generated by Django 2.0.3 on 2018-08-14 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_pizzarate'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subchoice', models.CharField(max_length=64)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('subsize', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_size', to='orders.Size')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='pizzarate',
            unique_together={('pizzatype', 'pizzasize', 'toppingtype')},
        ),
        migrations.AlterUniqueTogether(
            name='subrate',
            unique_together={('subchoice', 'subsize')},
        ),
    ]