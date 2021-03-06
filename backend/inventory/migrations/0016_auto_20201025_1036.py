# Generated by Django 3.1.2 on 2020-10-25 02:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0006_auto_20201025_0930'),
        ('inventory', '0015_auto_20201025_1011'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendor',
            old_name='def_description',
            new_name='default_description',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='def_exp_category',
        ),
        migrations.AddField(
            model_name='vendor',
            name='default_exp_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='ledger.expensecategory', verbose_name='Default expense category'),
        ),
    ]
