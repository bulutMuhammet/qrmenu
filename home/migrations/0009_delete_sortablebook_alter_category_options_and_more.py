# Generated by Django 4.2.4 on 2023-08-12 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_sortablebook'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SortableBook',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('order',), 'verbose_name': 'Kategori', 'verbose_name_plural': 'Kategoriler'},
        ),
        migrations.RenameField(
            model_name='category',
            old_name='my_order',
            new_name='order',
        ),
    ]
