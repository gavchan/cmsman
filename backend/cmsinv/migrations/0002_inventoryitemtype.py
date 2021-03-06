# Generated by Django 3.0.4 on 2020-03-29 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsinv', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryItemType',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('version', models.BigIntegerField(default=0)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'inventory_item_type',
                'managed': False,
            },
        ),
    ]
