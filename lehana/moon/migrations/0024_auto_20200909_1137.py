# Generated by Django 3.0.5 on 2020-09-09 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moon', '0023_remove_product_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='favourites',
        ),
        migrations.AddField(
            model_name='product',
            name='is_favourite',
            field=models.BooleanField(default=False, verbose_name='is_favourite'),
        ),
    ]