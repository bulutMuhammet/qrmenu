# Generated by Django 4.2.4 on 2023-08-12 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_product_detail_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
    ]