from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Settings(models.Model):
    title = models.CharField(max_length=155)
    description = RichTextField()
    title_cool = models.CharField(max_length=155)
    description_cool = RichTextField(verbose_name='Описание cool')
    title_mussion = models.CharField(max_length=155)
    image_mussion = models.ImageField(upload_to='settings')
    title_team = models.CharField(max_length=155)
    title_avenser = models.CharField(max_length=155)
    title_works = models.CharField(max_length=155)
    title_testimonials = models.CharField(max_length=155)
    title_about = models.CharField(max_length=155)
    title_contact = models.CharField(max_length=155)
    title_have = models.CharField(max_length=155)
    description_contact = RichTextField(verbose_name='Описание контакта')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Настройка Главной Страницы'

class Form(models.Model):
    name = models.CharField(max_length=155)
    info = models.CharField(max_length=255)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Формула обраного'