# Generated by Django 4.2.5 on 2023-09-13 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advapp', '0011_advreg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advreg',
            old_name='reg_age',
            new_name='AGE',
        ),
        migrations.RenameField(
            model_name='advreg',
            old_name='reg_name',
            new_name='NAME',
        ),
        migrations.RenameField(
            model_name='advreg',
            old_name='reg_phno',
            new_name='PHNO',
        ),
        migrations.RenameField(
            model_name='advreg',
            old_name='reg_weight',
            new_name='WEIGHT',
        ),
    ]