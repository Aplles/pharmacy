from django.db import models


class CartItem(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE, related_name='products',
                                verbose_name='Продукт')
    cart = models.ForeignKey("Cart", on_delete=models.CASCADE, related_name='item_carts',
                             verbose_name='Корзина')
    quantity = models.IntegerField(default=1, verbose_name='Количество')

    def __str__(self):
        return self.product.title

    class Meta:
        db_table = 'cartitems'
        app_label = "models_app"
        verbose_name = 'CartItem'
        verbose_name_plural = 'CartItems'
