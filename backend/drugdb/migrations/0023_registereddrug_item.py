# Generated by Django 3.1.3 on 2021-01-19 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0056_auto_20210116_1836'),
        ('drugdb', '0022_auto_20210110_0458'),
    ]

    operations = [
        migrations.AddField(
            model_name='registereddrug',
            name='item',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='inventory.item'),
        ),
    ]
