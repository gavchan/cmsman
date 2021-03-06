# Generated by Django 3.0.4 on 2020-04-19 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
        ('drugdb', '0004_auto_20200419_0426'),
    ]

    operations = [
        # This commented migration is recreated in 0006_drugdelivery.py; to be "--fake"d due to error of relation already existing
        # migrations.CreateModel(
        #     name='DrugDelivery',
        #     fields=[
        #         ('delivery_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='inventory.Delivery')),
        #         ('registration_no', models.CharField(blank=True, max_length=255, null=True)),
        #         ('items_unit', models.CharField(choices=[('AMPOULE', 'AMPOULE'), ('BOTTLE', 'BOTTLE'), ('BOX', 'BOX'), ('CAP', 'CAP'), ('DOSE', 'DOSE'), ('GRAM', 'GRAM'), ('INJECTION', 'INJECTION'), ('MG', 'MG'), ('ML', 'ML'), ('PACK', 'PACK'), ('TAB', 'TAB'), ('TUBE', 'TUBE'), ('UNIT', 'UNIT'), ('VIAL', 'VIAL')], default='TAB', max_length=100)),
        #     ],
        #     bases=('inventory.delivery',),
        # ),
        migrations.DeleteModel(
            name='DrugUnit',
        ),
        migrations.AlterModelOptions(
            name='registereddrug',
            options={'ordering': ['registration_no']},
        ),
        migrations.RenameField(
            model_name='registereddrug',
            old_name='permit_no',
            new_name='registration_no',
        ),
        migrations.AlterField(
            model_name='registereddrug',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='drugdb.Company'),
        ),
    ]
