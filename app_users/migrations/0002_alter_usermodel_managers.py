# Generated by Django 5.0.6 on 2024-11-24 09:20

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='usermodel',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
