# Generated by Django 3.0.8 on 2020-12-01 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0022_auto_20201201_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='status',
            field=models.CharField(blank=True, default='Free', max_length=50),
        ),
    ]