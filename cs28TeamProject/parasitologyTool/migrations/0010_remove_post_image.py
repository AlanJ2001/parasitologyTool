# Generated by Django 3.2.9 on 2021-12-20 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parasitologyTool', '0009_merge_0002_auto_20211218_1943_0008_auto_20211216_1833'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]
