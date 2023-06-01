from django.db import models


class Cart(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, verbose_name='Пользователь')

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'carts'
        app_label = "models_app"
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'
