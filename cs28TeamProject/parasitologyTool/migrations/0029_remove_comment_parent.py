# Generated by Django 3.2.9 on 2022-02-09 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parasitologyTool', '0028_comment_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='parent',
        ),
    ]
