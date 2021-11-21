# Generated by Django 3.2.5 on 2021-11-09 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parasitologyTool', '0002_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parasite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]