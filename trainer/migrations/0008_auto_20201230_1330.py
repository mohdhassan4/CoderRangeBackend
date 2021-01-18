# Generated by Django 3.0.8 on 2020-12-30 08:00

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0068_auto_20201230_1330'),
        ('trainer', '0007_auto_20201230_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussion',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 12, 30, 8, 0, 55, 490688, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='trainercourse',
            name='coaching_courseid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Courses'),
        ),
    ]
