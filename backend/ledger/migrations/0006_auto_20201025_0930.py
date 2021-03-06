# Generated by Django 3.1.2 on 2020-10-25 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0005_auto_20200516_1606'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ledgerentry',
            name='settled_date',
        ),
        migrations.AlterField(
            model_name='expense',
            name='payment_ref',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Cheque/ref no.'),
        ),
        migrations.AlterField(
            model_name='ledgerentry',
            name='expected_date',
            field=models.DateField(blank=True, null=True, verbose_name='Cheque/paid date'),
        ),
    ]
