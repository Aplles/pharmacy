# Generated by Django 4.2.1 on 2023-06-01 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('models_app', '0006_remove_cartitemorder_cart_item_cartitemorder_product_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='cart',
        ),
    ]
