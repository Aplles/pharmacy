from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(upload_to='img/category/', verbose_name='Изображение')
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name='categories',
                                 verbose_name='Категория')
    price = models.IntegerField(default=0, verbose_name='Цена')
    country = models.CharField(max_length=255, verbose_name='Страна производителя')

    RECEPT = 'Recept'
    NOT_RECEPT = 'not recept'

    VACATION_CHOICES = (
        (RECEPT, 'С рецептом'),
        (NOT_RECEPT, 'Без рецепта'),
    )
    vacation = models.CharField(max_length=20, choices=VACATION_CHOICES, verbose_name='Отпуск', default=NOT_RECEPT)
    expiration_date = models.CharField(max_length=50, verbose_name='Срок годности')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'products'
        app_label = "models_app"
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
