# Generated by Django 4.2.6 on 2023-11-07 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drinks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drink',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]