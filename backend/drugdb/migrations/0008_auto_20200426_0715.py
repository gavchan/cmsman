# Generated by Django 3.0.4 on 2020-04-25 23:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drugdb', '0007_auto_20200422_2152'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='registereddrug',
            options={'ordering': ['reg_no']},
        ),
        migrations.RenameField(
            model_name='company',
            old_name='date_modified',
            new_name='last_updated',
        ),
        migrations.RenameField(
            model_name='drugdelivery',
            old_name='registration_no',
            new_name='reg_no',
        ),
        migrations.RenameField(
            model_name='registereddrug',
            old_name='date_modified',
            new_name='last_updated',
        ),
        migrations.RenameField(
            model_name='registereddrug',
            old_name='registration_no',
            new_name='reg_no',
        ),
    ]
