# Generated by Django 4.1.3 on 2022-12-09 22:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='accountNumber',
            field=models.BigIntegerField(validators=[django.core.validators.MaxValueValidator(9999999999999999), django.core.validators.MinValueValidator(1000000000000000)]),
        ),
    ]
