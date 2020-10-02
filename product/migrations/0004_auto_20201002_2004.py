# Generated by Django 3.1.1 on 2020-10-02 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20201002_1824'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalePicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='sale_picture/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='SaleProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='sale_products/%Y/%m/%d')),
                ('name', models.CharField(max_length=250, verbose_name='Название товара')),
                ('description', models.TextField(verbose_name='Описание товара')),
                ('old_price', models.DecimalField(db_index=True, decimal_places=0, max_digits=10, verbose_name='Цена')),
                ('new_price', models.DecimalField(db_index=True, decimal_places=0, max_digits=10, verbose_name='Цена')),
                ('slug', models.SlugField(max_length=250)),
                ('availability_status', models.BooleanField(default=True, verbose_name='Наличие на складе')),
                ('sale_percent', models.PositiveSmallIntegerField(verbose_name='Скидка')),
            ],
            options={
                'verbose_name': 'Товар со скидкой',
                'verbose_name_plural': 'Товары со скидкой',
            },
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]
