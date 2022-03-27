# Generated by Django 3.2 on 2022-03-27 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trees', '0002_auto_20220327_0743'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('friendly_name', models.CharField(blank=True, max_length=254, null=True)),
                ('icon_fontawsome', models.CharField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='tree',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AddField(
            model_name='tree',
            name='feature',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='trees.feature'),
        ),
    ]
