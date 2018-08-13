# Generated by Django 2.0.3 on 2018-08-13 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PizzaRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('PizzaSize', models.ForeignKey(limit_choices_to={'id__in': ({'pk': 1}, {'pk': 2})}, on_delete=django.db.models.deletion.CASCADE, related_name='pizza_size', to='orders.Attr')),
                ('PizzaType', models.ForeignKey(limit_choices_to={'id__in': ({'pk': 4}, {'pk': 5})}, on_delete=django.db.models.deletion.CASCADE, related_name='pizza_type', to='orders.Attr')),
                ('ToppingType', models.ForeignKey(limit_choices_to={'id__in': ({'pk': 6}, {'pk': 7}, {'pk': 8}, {'pk': 9}, {'pk': 10})}, on_delete=django.db.models.deletion.CASCADE, related_name='topping_type', to='orders.Attr')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='pizzarate',
            unique_together={('PizzaType', 'PizzaSize', 'ToppingType')},
        ),
    ]