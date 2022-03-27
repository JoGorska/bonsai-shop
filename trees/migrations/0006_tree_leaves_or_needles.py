# Generated by Django 3.2 on 2022-03-27 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trees', '0005_rename_image_description_tree_image_alt'),
    ]

    operations = [
        migrations.AddField(
            model_name='tree',
            name='leaves_or_needles',
            field=models.CharField(blank=True, choices=[('coniferous', 'Coniferous'), ('deciduous', 'Deciduous')], default='coniferous', max_length=254, null=True),
        ),
    ]