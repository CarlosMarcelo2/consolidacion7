# Generated by Django 4.2.4 on 2023-08-22 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='directorgeneral',
            name='especialidad',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AddField(
            model_name='laboratorio',
            name='ciudad',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AddField(
            model_name='laboratorio',
            name='pais',
            field=models.CharField(default='', max_length=128),
        ),
    ]
