# Generated by Django 5.1.4 on 2025-01-10 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_remove_payment_pay_name_payment_supp_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='type',
            field=models.CharField(choices=[('cash', 'Cash'), ('online', 'Online')], max_length=10),
        ),
    ]
