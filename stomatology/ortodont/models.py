from django.db import models
from django.urls import reverse


class About(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='url', unique=True)

    def __str__(self):
        return self.title

    def get_url_about(self):
        return reverse('about', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'
        ordering = ['title']


class Contact(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='url', unique=True)

    def __str__(self):
        return self.title

    def get_url_contact(self):
        return reverse('contact', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
        ordering = ['title']


class Services(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='url', unique=True)

    def __str__(self):
        return self.title

    def get_url_services(self):
        return reverse('services', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Услуга(у)'
        verbose_name_plural = 'Услуги'
        ordering = ['title']


class Category(models.Model):
    fullName = models.CharField(max_length=255, verbose_name='Полное имя')
    phoneNumber = models.CharField(max_length=12, verbose_name='Номер телефона')
    email = models.EmailField(max_length=50, verbose_name='Почтовый ящик')
    CHOICES = (
        ('BZ', 'Боль в зубах'),
        ('BD', 'Боль в деснах'),
        ('NP', 'Неправильный прикус'),
        ('PZ', 'Потерян зуб'),
        ('PR', 'Прочее'),
    )
    disease = models.CharField(max_length=50, choices=CHOICES, verbose_name='Причина посещения')
    message = models.TextField(max_length=200, verbose_name='Описание проблемы')

    def __str__(self):
        return self.fullName

    class Meta:
        verbose_name = 'Категория(ю)'
        verbose_name_plural = 'Категории'
        ordering = ['fullName']