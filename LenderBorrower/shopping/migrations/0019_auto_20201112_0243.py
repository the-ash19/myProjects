# Generated by Django 3.1.3 on 2020-11-12 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0018_auto_20201112_0242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='mobile',
            field=models.CharField(max_length=10),
        ),
    ]