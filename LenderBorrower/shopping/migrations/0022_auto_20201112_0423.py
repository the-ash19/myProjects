# Generated by Django 3.1.3 on 2020-11-12 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0021_auto_20201112_0247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot',
            name='c1',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='slot',
            name='c2',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='slot',
            name='c3',
            field=models.IntegerField(default=0),
        ),
    ]
