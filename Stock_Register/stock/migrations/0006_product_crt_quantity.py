# Generated by Django 5.1.4 on 2025-01-10 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0005_remove_stock_sell_id_stock_buy_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='crt_quantity',
            field=models.ImageField(default=0, upload_to=''),
            preserve_default=False,
        ),
    ]