# Generated by Django 2.1.5 on 2020-11-18 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0027_auto_20201112_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='customer',
            name='time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='slot',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='slot',
            name='time',
            field=models.TimeField(),
        ),
    ]
