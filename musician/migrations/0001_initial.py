# Generated by Django 5.0.6 on 2024-06-01 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MusicianModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=20)),
                ('Last_name', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254)),
                ('Phone', models.CharField(max_length=12)),
                ('Instrument_Type', models.CharField(max_length=30)),
            ],
        ),
    ]
