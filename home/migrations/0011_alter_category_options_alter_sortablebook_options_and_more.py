# Generated by Django 4.2.4 on 2023-08-12 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_sortablebook'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['my_order']},
        ),
        migrations.AlterModelOptions(
            name='sortablebook',
            options={},
        ),
        migrations.RemoveField(
            model_name='category',
            name='order',
        ),
        migrations.RemoveField(
            model_name='sortablebook',
            name='my_order',
        ),
        migrations.AddField(
            model_name='category',
            name='my_order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
