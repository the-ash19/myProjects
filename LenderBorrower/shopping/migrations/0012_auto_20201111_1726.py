# Generated by Django 3.1.3 on 2020-11-11 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0011_auto_20201111_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='purpose',
            field=models.CharField(max_length=10),
        ),
    ]
