# Generated by Django 3.1.3 on 2020-11-12 01:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0015_auto_20201111_1749'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='sdata',
        ),
        migrations.AddField(
            model_name='customer',
            name='slot',
            field=models.ForeignKey(default=1007, on_delete=django.db.models.deletion.CASCADE, to='shopping.slot'),
        ),
        migrations.AddField(
            model_name='slot',
            name='c1',
            field=models.CharField(blank=True, max_length=21, null=True),
        ),
        migrations.AddField(
            model_name='slot',
            name='c2',
            field=models.CharField(blank=True, max_length=21, null=True),
        ),
        migrations.AddField(
            model_name='slot',
            name='c3',
            field=models.CharField(blank=True, max_length=21, null=True),
        ),
        migrations.AddField(
            model_name='slot',
            name='count',
            field=models.IntegerField(default=3),
        ),
        migrations.DeleteModel(
            name='SData',
        ),
    ]
