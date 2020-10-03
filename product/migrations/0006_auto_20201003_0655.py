# Generated by Django 3.1.1 on 2020-10-03 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20201002_2015'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SaleProduct',
        ),
        migrations.AddField(
            model_name='product',
            name='new_price',
            field=models.DecimalField(db_index=True, decimal_places=0, default=0, max_digits=10, verbose_name='Цена со скидкой'),
        ),
        migrations.AddField(
            model_name='product',
            name='sale_percent',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='sale_status',
            field=models.BooleanField(db_index=True, default=False),
        ),
    ]