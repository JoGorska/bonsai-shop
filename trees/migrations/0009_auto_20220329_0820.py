# Generated by Django 3.2 on 2022-03-29 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trees', '0008_auto_20220329_0802'),
    ]

    operations = [
        migrations.AddField(
            model_name='enviroment',
            name='aria_for_anchor',
            field=models.CharField(blank=True, default='Filter elements by', max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='feature',
            name='aria_for_anchor',
            field=models.CharField(blank=True, default='Filter elements by', max_length=254, null=True),
        ),
    ]
