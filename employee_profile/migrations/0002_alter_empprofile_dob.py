# Generated by Django 3.2.5 on 2022-05-26 17:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empprofile',
            name='Dob',
            field=models.DateField(default=datetime.date.today, max_length=8),
        ),
    ]