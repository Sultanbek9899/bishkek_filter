# Generated by Django 3.1.1 on 2020-10-01 02:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='product.category')),
            ],
            options={
                'verbose_name': 'Подкатегория',
                'verbose_name_plural': 'Подкатегории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products/%Y/%m/%d')),
                ('name', models.CharField(max_length=250, verbose_name='Название товара')),
                ('description', models.TextField(verbose_name='Описание товара')),
                ('price', models.DecimalField(db_index=True, decimal_places=0, max_digits=10, verbose_name='Цена')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата добавление')),
                ('slug', models.SlugField(max_length=250)),
                ('availability_status', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_categories', to='product.category', verbose_name='Категория товара')),
                ('sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_categories', to='product.category', verbose_name='Подкатегория товара')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['-created'],
            },
        ),
    ]
