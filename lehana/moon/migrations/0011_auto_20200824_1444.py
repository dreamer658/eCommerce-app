# Generated by Django 3.0.5 on 2020-08-24 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moon', '0010_auto_20200820_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(verbose_name="Nombre d'articles"),
        ),
    ]