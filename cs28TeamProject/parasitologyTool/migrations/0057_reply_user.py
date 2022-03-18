# Generated by Django 3.2.9 on 2022-03-18 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parasitologyTool', '0056_remove_reply_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='parasitologyTool.userprofile'),
        ),
    ]