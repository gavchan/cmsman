# Generated by Django 3.1.3 on 2021-01-01 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0052_item_vendor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
