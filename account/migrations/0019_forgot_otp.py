# Generated by Django 3.0.8 on 2020-10-10 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0018_auto_20201009_1802'),
    ]

    operations = [
        migrations.CreateModel(
            name='Forgot_otp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phonenumber', models.CharField(max_length=15)),
                ('otp', models.CharField(max_length=6)),
            ],
        ),
    ]