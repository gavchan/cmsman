# Generated by Django 3.0.4 on 2020-04-26 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_auto_20200426_0640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='bonus_quantity',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='purchase_quantity',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=10),
        ),
    ]
