# Generated by Django 3.2 on 2022-04-16 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_auto_20220415_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='newsletter',
            field=models.IntegerField(choices=[(0, 'Not Interested'), (1, 'Sign me up')], default=0),
        ),
    ]
