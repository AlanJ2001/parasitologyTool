# Generated by Django 2.2.17 on 2022-01-18 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parasitologyTool', '0017_auto_20220115_0649'),
    ]

    operations = [
        migrations.AddField(
            model_name='parasite',
            name='intro',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
    ]