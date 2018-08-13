# Generated by Django 2.0.3 on 2018-08-13 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0016_auto_20180813_1955'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubsRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SubsChoice', models.CharField(max_length=64)),
                ('Price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('SubsSize', models.ForeignKey(limit_choices_to={'id__in': ({'pk': 1}, {'pk': 2}, {'pk': 3})}, on_delete=django.db.models.deletion.CASCADE, related_name='subs_size', to='orders.Attr')),
                ('SubsType', models.ForeignKey(limit_choices_to={'id__in': ({'pk': 34}, {'pk': 35})}, on_delete=django.db.models.deletion.CASCADE, related_name='subs_type', to='orders.Attr')),
            ],
        ),
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
