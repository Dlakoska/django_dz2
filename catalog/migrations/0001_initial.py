# Generated by Django 5.1 on 2024-09-08 06:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование категории')),
                ('description', models.TextField(help_text='Введите описание категории', verbose_name='Описание категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(help_text='Введите описание продукта', verbose_name='Описание продукта')),
                ('image', models.ImageField(blank=True, help_text='Загрузите фото товара', null=True, upload_to='images/', verbose_name='Фото')),
                ('category', models.CharField(help_text='Введите категорию продукта', max_length=100, verbose_name='Категория')),
                ('price', models.IntegerField(verbose_name='Цена за покупку')),
                ('created_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата создания(записи в БД)')),
                ('updated_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата последнего изменения(записи в БД)')),
                ('name', models.ForeignKey(help_text='Введите название продукта', on_delete=django.db.models.deletion.CASCADE, to='catalog.category', verbose_name='Наименование продукта')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'ordering': ['name', '-created_at'],
            },
        ),
    ]