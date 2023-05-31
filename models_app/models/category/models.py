from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(upload_to='img/category/', verbose_name='Изображение')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'categories'
        app_label = "models_app"
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
