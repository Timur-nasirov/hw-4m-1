from django.db import models

# Create your models here.
class Blog(models.Model):
    author = models.CharField(
        verbose_name='Автор',
        max_length=255,
    )
    date = models.DateField(
        verbose_name='Дата создания',
        auto_now_add=True,
        blank=True
    )
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=255
    )
    content = models.TextField(
        verbose_name='Содержание'
    )
    tags = models.CharField(
        verbose_name='Тэги',
        max_length=255
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'

class Comment(models.Model):
    author = models.CharField(
        verbose_name='Автор',
        max_length=255,
    )
    content = models.TextField(
        verbose_name='Комментарий'
    )
    blog = models.ForeignKey(
        Blog, 
        on_delete=models.CASCADE,
        verbose_name='Блог'
    )

    def __str__(self):
        return self.author
    
    class Meta:
        verbose_name = 'Комментарий к блогу'
        verbose_name_plural = 'Комменатрии к блогам'