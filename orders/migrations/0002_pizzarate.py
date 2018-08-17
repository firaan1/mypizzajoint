# Generated by Django 2.0.3 on 2018-08-14 17:18

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
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('pizzasize', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pizza_size', to='orders.Size')),
                ('pizzatype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pizza_type', to='orders.PizzaType')),
                ('toppingtype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topping_type', to='orders.ToppingType')),
            ],
        ),
    ]