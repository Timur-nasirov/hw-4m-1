from django.db import models

# Create your models here.

class ShopCategory(models.Model):
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=255
    )
    count = models.SmallIntegerField(
        verbose_name='Количество товаров'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class ShopProduct(models.Model):
    title = models.CharField(
        verbose_name='Имя продукта',
        max_length=100
    )
    description = models.TextField(
        verbose_name='Полное описание'
    )
    short_desc = models.TextField(
        verbose_name='Короткое описание'
    )
    image = models.ImageField(
        verbose_name='Картинка',
        upload_to='products/'
    )
    new_price = models.SmallIntegerField(
        verbose_name='Цена продукта со скидкой'
    )
    old_price = models.SmallIntegerField(
        verbose_name='Цена продукта без скидки'
    )
    category = models.ForeignKey(
        ShopCategory,
        on_delete=models.CASCADE,
        verbose_name='Категория'
    )
    tags = models.CharField(
        verbose_name='Тэги',
        max_length=255
    )
    sku = models.CharField(
        verbose_name='SKU',
        max_length=255
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

class ShopDish(models.Model):
    title = models.CharField(
        verbose_name='Название продукта',
        max_length=150
    )
    description = models.TextField(
        verbose_name='Описание продукта'
    )
    new_price = models.SmallIntegerField(
        verbose_name='Цена продукта со скидкой'
    )
    old_price = models.SmallIntegerField(
        verbose_name='Цена продукта без скидки'
    )
    category = models.ForeignKey(
        ShopCategory,
        on_delete=models.CASCADE,
        verbose_name='Категория'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'

class Pay(models.Model):
    name = models.CharField(
        verbose_name='Имя',
        max_length=255
    )
    surname = models.CharField(
        verbose_name='Фамилия',
        max_length=255
    )
    phone = models.CharField(
        verbose_name='Телефон',
        max_length=30
    )
    address = models.CharField(
        verbose_name='Адрес',
        max_length=255
    )
    email = models.EmailField(
        verbose_name='Email'
    )
    city = models.CharField(
        verbose_name='Город',
        max_length=50
    )
    country = models.CharField(
        verbose_name='Код страны',
        max_length=2
    )
    domofon = models.CharField(
        verbose_name='Домофон',
        max_length=30
    )

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Оплата'
        verbose_name_plural = 'Оплаты'

class Menu(models.Model):
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=255
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    new_price = models.SmallIntegerField(
        verbose_name='Новая цена'
    )
    old_price = models.SmallIntegerField(
        verbose_name='Старая цена'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

class ProductComment(models.Model):
    name = models.CharField(
        verbose_name='Имя',
        max_length=255
    )
    content = models.TextField(
        verbose_name='Содержание'
    )
    product = models.ForeignKey(
        ShopProduct,
        verbose_name='Продукт',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Коментраий к продукту'
        verbose_name_plural = 'Комментарии к продуктами'