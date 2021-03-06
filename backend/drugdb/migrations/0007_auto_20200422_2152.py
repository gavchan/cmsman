# Generated by Django 3.0.4 on 2020-04-22 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drugdb', '0006_drugdelivery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drugdelivery',
            name='items_unit',
            field=models.CharField(choices=[('AMPOULE', 'Ampoule'), ('BOTTLE', 'Bottle'), ('BOX', 'Box'), ('CAP', 'Cap'), ('DOSE', 'Dose'), ('GRAM', 'gram'), ('INJECTION', 'Injection'), ('MG', 'mg'), ('ML', 'mL'), ('PACK', 'Pack'), ('TAB', 'Tablet'), ('TUBE', 'Tube'), ('UNIT', 'Unit'), ('VIAL', 'Vial')], default='TAB', max_length=100),
        ),
    ]
