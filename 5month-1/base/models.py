from django.db import models

# Create your models here.
class Settings(models.Model):
    title = models.CharField(
        verbose_name='Заголовок сайта',
        max_length=100
    )
    logo = models.ImageField(
        verbose_name='Логотип сайта',
        upload_to='settings/logo/'
    )
    banner_1 = models.ImageField(
        verbose_name='Первый банер на главой странице',
        upload_to='settings/banner/'
    )
    title_1 = models.CharField(
        verbose_name='Первый заголовок на главной странице',
        max_length=255
    )
    description_1 = models.TextField(
        verbose_name='Первый текст на главной странице'
    )
    banner_2 = models.ImageField(
        verbose_name='Второй банер на главой странице',
        upload_to='settings/banner2/'
    )
    title_2 = models.CharField(
        verbose_name='Второй заголовок на главной странице',
        max_length=255
    )
    description_2 = models.TextField(
        verbose_name='Второй текст на главной странице'
    )
    title_3 = models.CharField(
        verbose_name='Третий заголовок на главной странице',
        max_length=255
    )
    description_3 = models.TextField(
        verbose_name='Третий текст на главной странице'
    )
    quality_1 = models.CharField(
        verbose_name='Первое качество',
        max_length=50
    )
    quality_desc_1 = models.CharField(
        verbose_name='Описание первого качества',
        max_length=100
    )
    quality_2 = models.CharField(
        verbose_name='Второе качество',
        max_length=50
    )
    quality_desc_2 = models.CharField(
        verbose_name='Описание второго качества',
        max_length=100
    )
    quality_3 = models.CharField(
        verbose_name='Третье качество',
        max_length=50
    )
    quality_desc_3 = models.CharField(
        verbose_name='Описание третьего качества',
        max_length=100
    )
    quality_4 = models.CharField(
        verbose_name='Четвертое качество',
        max_length=50
    )
    quality_desc_4 = models.CharField(
        verbose_name='Описание четвертого качества',
        max_length=100
    )
    copyright = models.CharField(
        verbose_name='Текст copyright',
        max_length=255
    )
    loader = models.ImageField(
        verbose_name='Картинка загрузки',
        upload_to='settings/loader/'
    )
    description_bottom = models.TextField(
        verbose_name='Описание снизу'
    )
    logo_bottom = models.ImageField(
        verbose_name='Логотип снизу',
        upload_to='settings/bottom_logo/'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Настройка сайта'
        verbose_name_plural = 'Настройки сайта'

class Galery(models.Model):
    photo = models.ImageField(
        verbose_name='Фото',
        upload_to='galery/'
    )
    title = models.CharField(
        verbose_name='Название картинки',
        max_length=255
    )
    link = models.URLField(
        verbose_name='Ссылка'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фото в галереи'
        verbose_name_plural = 'Фото в галерее'

class Contact(models.Model):
    title = models.CharField(
        verbose_name='Название',
        max_length=255
    )
    instagram = models.URLField(
        verbose_name='Ссылка на инстаграм',
        null=True, blank=True
    )
    youtube = models.URLField(
        verbose_name='Ссылка на ютуб',
        null=True, blank=True
    )
    telegram = models.URLField(
        verbose_name='Ссылка на телеграм',
        null=True, blank=True
    )

    phone_1 = models.CharField(
        verbose_name='Телефон 1',
        max_length=25,
        null=True, blank=True
    )
    phone_2 = models.CharField(
        verbose_name='Телефон 2',
        max_length=25,
        null=True, blank=True
    )
    email_1 = models.EmailField(
        verbose_name='Email 1',
        null=True, blank=True
    )
    email_2 = models.EmailField(
        verbose_name='Email 2',
        null=True, blank=True
    )
    address = models.CharField(
        verbose_name='Адрес',
        max_length=100,
        null=True, blank=True
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

class Error(models.Model):
    title = models.CharField(
        verbose_name='Заголовок ошибки',
        max_length=255
    )
    description = models.TextField(
        verbose_name='Текст ошибки'
    )
    image = models.ImageField(
        verbose_name='Картинка ошибки',
        upload_to='error/'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Настройка ошибки 404'
        verbose_name_plural = 'Настройки ошибок 404'

class About(models.Model):
    title_1 = models.CharField(
        verbose_name='Заголовок 1',
        max_length=255
    )
    description_1 = models.TextField(
        verbose_name='Описание 1'
    )
    banner_1 = models.ImageField(
        verbose_name='Баннер 1',
        upload_to='about/banner/'
    )
    title_2 = models.CharField(
        verbose_name='Заголовок 2',
        max_length=255
    )
    description_2 = models.TextField(
        verbose_name='Описание 2'
    )
    banner_2 = models.ImageField(
        verbose_name='Баннер 2',
        upload_to='about/banner/'
    )
    def __str__(self):
        return self.title_1
    
    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'


class Coming(models.Model):
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=255
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        verbose_name='Картинка',
        upload_to='coming/'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Настройка страницы coming soon'
        verbose_name_plural = 'Настройки страниц coming soon'


class HelpMessage(models.Model):
    name = models.CharField(
        verbose_name='Имя',
        max_length=255
    )
    email = models.EmailField(
        verbose_name='Email'
    )
    quest = models.CharField(
        verbose_name='Вопрос',
        max_length=255
    )
    message = models.TextField(
        verbose_name='Сообщение'
    )

    def __str__(self):
        return self.quest
    
    class Meta:
        verbose_name = 'Обращение в поддержку'
        verbose_name_plural = 'Обращения в поддержку'

class Faq(models.Model):
    title_1 = models.CharField(
        verbose_name='Заголовок 1',
        max_length=255
    )
    desc_1 = models.TextField(
        verbose_name='Описание 1'
    )
    title_2 = models.CharField(
        verbose_name='Заголовок 2',
        max_length=255
    )
    desc_2 = models.TextField(
        verbose_name='Описание 2'
    )
    title_3 = models.CharField(
        verbose_name='Заголовок 3',
        max_length=255
    )
    desc_3 = models.TextField(
        verbose_name='Описание 3'
    )
    title_4 = models.CharField(
        verbose_name='Заголовок 4',
        max_length=255
    )
    desc_4 = models.TextField(
        verbose_name='Описание 4'
    )
    title_5 = models.CharField(
        verbose_name='Заголовок 5',
        max_length=255
    )
    desc_5 = models.TextField(
        verbose_name='Описание 5'
    )
    def __str__(self):
        return self.title_1
    
    class Meta:
        verbose_name = 'Настройка FAQ'
        verbose_name_plural = 'Настройки FAQ'

class SettingsTwo(models.Model):
    prev_title = models.CharField(
        verbose_name='Верхний заголовок',
        max_length=150
    )
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=255
    )
    old_price = models.SmallIntegerField(
        verbose_name='Старая цена'
    )
    new_price = models.SmallIntegerField(
        verbose_name='Новая цена'
    )

    title_banner = models.CharField(
        verbose_name='Заголовок баннера',
        max_length=255
    )
    desc_banner = models.TextField(
        verbose_name='Описание баннера'
    )
    image_banner = models.ImageField(
        verbose_name='Картинка баннера',
        upload_to='settings2/'
    )
    video = models.URLField(
        verbose_name='Ссылка на видео "как зарегестрироваться"'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Настройка второй главной страницы'
        verbose_name_plural = 'Настройки второй главной страницы'

class SettingsThree(models.Model):
    title_1 = models.CharField(
        verbose_name='Заголовок 1',
        max_length=255
    )
    desc_1 = models.TextField(
        verbose_name='Описание 1'
    )
    image_1 = models.ImageField(
        verbose_name='Баннер 1',
        upload_to='settings3/banner1/'
    )

    title_2 = models.CharField(
        verbose_name='Заголовок 2',
        max_length=255
    )
    desc_2 = models.TextField(
        verbose_name='Описание 2'
    )
    image_2 = models.ImageField(
        verbose_name='Баннер 2',
        upload_to='settings3/banner2/'
    )

    customers = models.SmallIntegerField(
        verbose_name='Количеcтво клиентов'
    )
    outlet = models.SmallIntegerField(
        verbose_name='Количетсво торговых точек'
    )
    satis = models.SmallIntegerField(
        verbose_name='Процент удовлетворения клиентов'
    )

    def __str__(self):
        return self.title_1

    class Meta:
        verbose_name = 'Настройка третей главной страницы'
        verbose_name_plural = 'Настройки третей главной страницы'

class SettingsFour(models.Model):
    title_1 = models.CharField(
        verbose_name='Заголовок 1',
        max_length=255
    )
    desc_1 = models.TextField(
        verbose_name='Описание 1'
    )
    banner_1 = models.ImageField(
        verbose_name='Баннер 1',
        upload_to='settings4/banner1/'
    )

    title_2 = models.CharField(
        verbose_name='Заголовок 2',
        max_length=255
    )
    banner_2 = models.ImageField(
        verbose_name='Баннер 2',
        upload_to='settings4/banner2/'
    )
    
    def __str__(self):
        return self.title_1

    class Meta:
        verbose_name = 'Настройка четвертой главной страницы'
        verbose_name_plural = 'Настройки четвертой главной страницы'

class SettingsFive(models.Model):
    title_1 = models.CharField(
        verbose_name='Заголовок 1',
        max_length=255
    )
    image_1 = models.ImageField(
        verbose_name='Баннер 1',
        upload_to='settings5/banner1/'
    )
    minititle = models.CharField(
        verbose_name='Мини заголовок 1',
        max_length=50
    )
    new_price = models.SmallIntegerField(
        verbose_name='Новая цена'
    )
    old_price = models.SmallIntegerField(
        verbose_name='Старая цена'
    )

    title_2 = models.CharField(
        verbose_name='Заголовок 2',
        max_length=255
    )
    desc_2 = models.TextField(
        verbose_name='Описание 2'
    )
    image_2 = models.ImageField(
        verbose_name='Баннер 2',
        upload_to='settings5/banner2/'
    )

    def __str__(self):
        return self.title_1
    
    class Meta:
        verbose_name = 'Настройка пятой главной страницы'
        verbose_name_plural = 'Настройки пятой главной страницы'

class Reservation(models.Model):
    name = models.CharField(
        verbose_name='Имя клиента',
        max_length=255
    )
    email = models.EmailField(
        verbose_name='Email'
    )
    person = models.SmallIntegerField(
        verbose_name='Количество человек'
    )
    phone = models.CharField(
        verbose_name='Телефон',
        max_length=40
    )
    date = models.DateField(
        verbose_name='Дата бронирования',
        auto_now_add=True
    )
    time = models.TimeField(
        verbose_name='Время бронирования',
        auto_now_add=True
    )
    message = models.TextField(
        verbose_name='Сообщение',
        null=True,
        blank=True
    )
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'

class Terms(models.Model):
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=255
    )
    content = models.TextField(
        verbose_name='Политика конфиденциальности'
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Политика конфиденциальности'
        verbose_name_plural = 'Политики конфиденциальности'