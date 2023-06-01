# Generated by Django 4.2.1 on 2023-06-01 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models_app', '0007_remove_order_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Ready', 'Готов'), ('Not ready', 'Не готов')], default='Not ready', max_length=20, verbose_name='Отпуск'),
        ),
    ]
