# Generated by Django 3.2.18 on 2023-05-31 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models_app', '0003_product_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.IntegerField(default=10, verbose_name='Сумма заказа'),
            preserve_default=False,
        ),
    ]
