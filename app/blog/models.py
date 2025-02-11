from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=155)
    image = models.ImageField(upload_to='blog')
    date = models.CharField(max_length=10)
    text1 = RichTextField(verbose_name='Текст', null=True, blank=True)
    image1 = models.ImageField(upload_to='blog', null=True, blank=True)
    image2 = models.ImageField(upload_to='blog', null=True, blank=True)
    text2 = RichTextField(verbose_name='Текст', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Блог'


class Comment(models.Model):
    name = models.CharField(
        max_length=155,
        verbose_name='Имя'
    )
    email = models.EmailField(
        verbose_name='Почта'
    )
    message = models.TextField(
        verbose_name='Сообщение'
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Комментарий'