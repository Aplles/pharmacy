# Generated by Django 4.2.1 on 2023-06-01 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('models_app', '0005_cartitemorder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitemorder',
            name='cart_item',
        ),
        migrations.AddField(
            model_name='cartitemorder',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='models_app.product', verbose_name='Продукт'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cartitemorder',
            name='quantity',
            field=models.IntegerField(default=1, verbose_name='Количество'),
        ),
    ]
