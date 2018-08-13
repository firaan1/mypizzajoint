# Generated by Django 2.0.3 on 2018-08-13 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20180813_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizzarate',
            name='PizzaSize',
            field=models.ForeignKey(limit_choices_to={'id__in': ({'pk': 1}, {'pk': 2})}, on_delete=django.db.models.deletion.CASCADE, related_name='pizza_size', to='orders.Attr'),
        ),
        migrations.AlterField(
            model_name='pizzarate',
            name='PizzaType',
            field=models.ForeignKey(limit_choices_to={'id__in': ({'pk': 4}, {'pk': 5})}, on_delete=django.db.models.deletion.CASCADE, related_name='pizza_type', to='orders.Attr'),
        ),
        migrations.AlterField(
            model_name='pizzarate',
            name='ToppingType',
            field=models.ForeignKey(limit_choices_to={'id__in': ({'pk': 6}, {'pk': 7}, {'pk': 8}, {'pk': 9}, {'pk': 10})}, on_delete=django.db.models.deletion.CASCADE, related_name='topping_type', to='orders.Attr'),
        ),
    ]
