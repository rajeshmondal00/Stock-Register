# Generated by Django 5.1.4 on 2025-01-10 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0006_product_crt_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='crt_quantity',
            field=models.IntegerField(),
        ),
    ]