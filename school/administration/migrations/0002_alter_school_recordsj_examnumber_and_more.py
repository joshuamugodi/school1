# Generated by Django 4.0.5 on 2022-06-16 15:13

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school_recordsj',
            name='Examnumber',
            field=models.CharField(max_length=12, primary_key=True, serialize=False, verbose_name=django.contrib.auth.models.User),
        ),
        migrations.AlterField(
            model_name='school_recordss',
            name='Examnumber',
            field=models.CharField(max_length=12, primary_key=True, serialize=False, verbose_name=django.contrib.auth.models.User),
        ),
    ]
