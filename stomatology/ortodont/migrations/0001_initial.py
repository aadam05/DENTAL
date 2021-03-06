# Generated by Django 3.2.4 on 2021-06-16 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='url')),
            ],
            options={
                'verbose_name': 'О нас',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=255, verbose_name='Полное имя')),
                ('phoneNumber', models.CharField(max_length=12, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=50, verbose_name='Почтовый ящик')),
                ('disease', models.CharField(choices=[('BZ', 'Боль в зубах'), ('BD', 'Боль в деснах'), ('NP', 'Неправильный прикус'), ('PZ', 'Потерян зуб'), ('PR', 'Прочее')], max_length=50, verbose_name='Причина посещения')),
                ('message', models.TextField(max_length=200, verbose_name='Описание проблемы')),
            ],
            options={
                'verbose_name': 'Категория(ю)',
                'verbose_name_plural': 'Категории',
                'ordering': ['fullName'],
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='url')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='url')),
            ],
            options={
                'verbose_name': 'Услуга(у)',
                'verbose_name_plural': 'Услуги',
                'ordering': ['title'],
            },
        ),
    ]
