# Generated by Django 3.2 on 2022-03-27 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tree',
            name='current_stock',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tree',
            name='name',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
