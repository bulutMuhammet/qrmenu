# Generated by Django 4.2.4 on 2023-08-12 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_category_title_en_product_detail_en_product_title_en'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='my_order',
            field=models.PositiveIntegerField(default=0, verbose_name='Sıra'),
        ),
    ]