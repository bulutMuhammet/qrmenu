# Generated by Django 4.2.4 on 2023-08-12 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0.0, verbose_name='Ürün Fiyatı'),
        ),
    ]