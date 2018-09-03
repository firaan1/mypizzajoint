# Generated by Django 2.0.3 on 2018-08-20 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_placedorder_completed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='placedorder',
            name='orderdinnerplatter',
        ),
        migrations.AddField(
            model_name='placedorder',
            name='orderdinnerplatter',
            field=models.ManyToManyField(related_name='order_dinnerplatter', to='orders.OrderDinnerPlatter'),
        ),
        migrations.RemoveField(
            model_name='placedorder',
            name='orderpasta',
        ),
        migrations.AddField(
            model_name='placedorder',
            name='orderpasta',
            field=models.ManyToManyField(related_name='order_pasta', to='orders.OrderPasta'),
        ),
        migrations.RemoveField(
            model_name='placedorder',
            name='orderpizza',
        ),
        migrations.AddField(
            model_name='placedorder',
            name='orderpizza',
            field=models.ManyToManyField(related_name='order_pizza', to='orders.OrderPizza'),
        ),
        migrations.RemoveField(
            model_name='placedorder',
            name='ordersalad',
        ),
        migrations.AddField(
            model_name='placedorder',
            name='ordersalad',
            field=models.ManyToManyField(related_name='order_salad', to='orders.OrderSalad'),
        ),
        migrations.RemoveField(
            model_name='placedorder',
            name='ordersub',
        ),
        migrations.AddField(
            model_name='placedorder',
            name='ordersub',
            field=models.ManyToManyField(related_name='order_sub', to='orders.OrderSub'),
        ),
    ]