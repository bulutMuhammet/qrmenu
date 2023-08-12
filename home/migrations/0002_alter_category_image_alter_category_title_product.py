# Generated by Django 4.2.4 on 2023-08-12 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='categories/', verbose_name='Kategori Görseli'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=60, verbose_name='Kategori İsmi'),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Ürün İsmi')),
                ('image', models.ImageField(upload_to='categories/product', verbose_name='Ürün Görseli')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='home.category', verbose_name='Kategori')),
            ],
            options={
                'verbose_name': 'Ürün',
                'verbose_name_plural': 'Ürünler',
            },
        ),
    ]
