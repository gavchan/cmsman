# Generated by Django 3.1.3 on 2020-11-14 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0039_auto_20201114_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='cms',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
