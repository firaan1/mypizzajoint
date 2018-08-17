# Generated by Django 2.0.3 on 2018-08-14 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_dinnerplatterrate_pastarate_saladrate'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderPizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizzachoice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pizza_choice', to='orders.PizzaRate')),
                ('toppingchoice', models.ManyToManyField(blank=True, null=True, related_name='pizza_topping', to='orders.ToppingChoice')),
            ],
        ),
    ]