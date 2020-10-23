# Generated by Django 3.0.5 on 2020-10-17 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moon', '0045_auto_20201017_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessory',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='moon.Product', verbose_name='Produit'),
        ),
        migrations.AlterField(
            model_name='clothes',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='moon.Product', verbose_name='Produit'),
        ),
        migrations.AlterField(
            model_name='shoes',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='moon.Product', verbose_name='Produit'),
        ),
        migrations.AlterField(
            model_name='variation',
            name='category',
            field=models.CharField(choices=[('size', 'size'), ('color', 'color'), ('package', 'package')], default='size', max_length=50),
        ),
    ]
