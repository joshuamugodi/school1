# Generated by Django 3.2.9 on 2022-05-31 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='school_recordsJ',
            fields=[
                ('firstname', models.CharField(max_length=40)),
                ('lastname', models.CharField(max_length=40)),
                ('Class', models.CharField(max_length=3)),
                ('Examnumber', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('g7', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='school_recordsS',
            fields=[
                ('firstname', models.CharField(max_length=40)),
                ('lastname', models.CharField(max_length=40)),
                ('Class', models.CharField(max_length=3)),
                ('Examnumber', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('g9', models.CharField(max_length=3)),
            ],
        ),
    ]
