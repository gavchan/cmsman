# Generated by Django 3.1.2 on 2020-11-03 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0025_auto_20201103_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveryorder',
            name='delivery_items',
            field=models.ManyToManyField(blank=True, through='inventory.DeliveryItems', to='inventory.Item'),
        ),
    ]
