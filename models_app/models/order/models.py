from django.db import models


class Order(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name='users',
                             verbose_name='Пользователь')
    number = models.CharField(max_length=255, verbose_name='Номер заказа')
    adress = models.CharField(max_length=255, verbose_name='Адрес доставки')
    total_price = models.IntegerField(verbose_name='Сумма заказа')
    READY = 'Ready'
    NOT_READY = 'Not ready'

    STATUS_CHOICES = (
        (READY, 'Готов'),
        (NOT_READY, 'Не готов'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, verbose_name='Статус', default=NOT_READY)

    def __str__(self):
        return self.number

    class Meta:
        db_table = 'orders'
        app_label = "models_app"
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class CartItemOrder(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE, verbose_name='Продукт')
    order = models.ForeignKey("Order", on_delete=models.CASCADE, verbose_name='Заказ')
    quantity = models.IntegerField(default=1, verbose_name='Количество')

    def __str__(self):
        return f"{self.product.title} {self.order.number}"

    class Meta:
        db_table = 'cart_items_orders'
        app_label = "models_app"
        verbose_name = 'CartItemOrder'
        verbose_name_plural = 'CartItemsOrders'
