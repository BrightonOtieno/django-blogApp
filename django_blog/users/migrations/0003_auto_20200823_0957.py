# Generated by Django 3.1 on 2020-08-23 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200823_0900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='hobby',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
