# Generated by Django 3.0.8 on 2020-09-27 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20200927_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='phonenumber',
            field=models.CharField(default='', max_length=15),
            preserve_default=False,
        ),
    ]