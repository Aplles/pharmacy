from django.db import models


class Order(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name='users',
                             verbose_name='Пользователь')
    number = models.CharField(max_length=255, verbose_name='Номер заказа')
    cart = models.ForeignKey("Cart", on_delete=models.CASCADE, related_name='carts',
                             verbose_name='Корзина')
    adress = models.CharField(max_length=255, verbose_name='Адрес доставки')
    total_price = models.IntegerField(verbose_name='Сумма заказа')

    def __str__(self):
        return self.number

    class Meta:
        db_table = 'orders'
        app_label = "models_app"
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class CartItemOrder(models.Model):
    cart_item = models.ForeignKey("CartItem", on_delete=models.CASCADE, verbose_name='Продукт')
    order = models.ForeignKey("Order", on_delete=models.CASCADE, verbose_name='Заказ')

    def __str__(self):
        return f"{self.cart_item} {self.order}"

    class Meta:
        db_table = 'cart_items_orders'
        app_label = "models_app"
        verbose_name = 'CartItemOrder'
        verbose_name_plural = 'CartItemsOrders'
