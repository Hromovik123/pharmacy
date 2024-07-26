# Generated by Django 4.2.7 on 2023-12-01 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_remove_order_delivery_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
    ]