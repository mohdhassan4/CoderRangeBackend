# Generated by Django 3.0.8 on 2020-12-01 12:46

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0057_auto_20201201_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batchtype',
            name='coursesId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Courses'),
        ),
        migrations.AlterField(
            model_name='certification',
            name='coursesId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Courses'),
        ),
        migrations.AlterField(
            model_name='course_info',
            name='coursesId',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.Courses'),
        ),
        migrations.AlterField(
            model_name='democlass',
            name='coursesId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Courses'),
        ),
        migrations.AlterField(
            model_name='democlass_otp',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 1, 12, 46, 9, 486167, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='helpdesk',
            name='coursesId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Courses'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='coursesId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Courses'),
        ),
        migrations.AlterField(
            model_name='refund',
            name='coursesId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Courses'),
        ),
        migrations.AlterField(
            model_name='solutiondesk',
            name='queryId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Helpdesk'),
        ),
    ]
