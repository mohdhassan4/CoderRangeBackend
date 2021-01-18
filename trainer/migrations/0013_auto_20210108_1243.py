# Generated by Django 3.0.8 on 2021-01-08 07:13

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0073_auto_20210108_1243'),
        ('trainer', '0012_auto_20210104_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class_review',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 1, 8, 7, 13, 31, 361801, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='discussion',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 1, 8, 7, 13, 31, 362799, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='trainercourse',
            name='coaching_courseid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Courses'),
        ),
    ]