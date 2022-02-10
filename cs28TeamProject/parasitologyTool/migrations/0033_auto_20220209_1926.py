# Generated by Django 3.2.9 on 2022-02-09 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parasitologyTool', '0032_auto_20220209_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='clinical_post',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='parasitologyTool.post'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='parasitologyTool.researchpost'),
        ),
    ]
