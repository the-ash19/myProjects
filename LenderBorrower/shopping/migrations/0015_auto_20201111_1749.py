# Generated by Django 3.1.3 on 2020-11-11 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0014_product_idd'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='p10',
        ),
        migrations.AlterField(
            model_name='product',
            name='idd',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]
