# Generated by Django 3.0.4 on 2020-04-23 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20200423_1949'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['name']},
        ),
        migrations.RenameField(
            model_name='item',
            old_name='product_name',
            new_name='name',
        ),
    ]
