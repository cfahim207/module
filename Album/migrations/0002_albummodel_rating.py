# Generated by Django 5.0.6 on 2024-06-01 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Album', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='albummodel',
            name='Rating',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default=1, max_length=50),
        ),
    ]
