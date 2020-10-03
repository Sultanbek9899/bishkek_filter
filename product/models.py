from django.db import models


# Create your models here.


class Category(models.Model):
    """Модель для категорий товара"""
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    """Модель дял подкатегорий товара"""
    category = models.ForeignKey(Category, related_name='child_categories',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return self.name


class Product(models.Model):
    """Модель для товара магазина"""
    category = models.ForeignKey(Category,
                                 related_name='product_categories',
                                 on_delete=models.CASCADE,
                                 verbose_name='Категория товара')
    sub_category = models.ForeignKey(SubCategory,
                                     related_name='sub_categories',
                                     on_delete=models.CASCADE,
                                     verbose_name='Подкатегория товара')

    image = models.ImageField(upload_to='products/%Y/%m/%d')
    name = models.CharField(max_length=250, verbose_name='Название товара')
    description = models.TextField(verbose_name='Описание товара')
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Цена', db_index=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавление', db_index=True)
    slug = models.SlugField(max_length=250)  # на будущее, если для товара нужна будет страница
    availability_status = models.BooleanField(default=True, verbose_name='Наличие на складе')
    # Продукт может быть и скидочным , если статус будет True
    sale_status = models.BooleanField(default=False, db_index=True,
                                      verbose_name='Статус скидки товара')
    new_price = models.DecimalField(max_digits=10, default=0, decimal_places=0,
                                    verbose_name='Цена со скидкой', db_index=True)
    sale_percent = models.PositiveSmallIntegerField(default=0, verbose_name='Процент скидки')

    class Meta:
        ordering = ['-created']
        verbose_name = 'Товар'
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name




class SalePicture(models.Model):
    image = models.ImageField(upload_to='sale_picture/%Y/%m/%d')

