# Generated by Django 3.0.8 on 2020-08-17 05:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='last_login',
            field=models.DateField(default=datetime.datetime(2020, 8, 17, 5, 28, 45, 679588, tzinfo=utc)),
        ),
    ]