# Generated by Django 3.0.8 on 2020-10-19 08:17

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0044_auto_20201019_1248'),
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
            model_name='class_activity',
            name='coursesId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Courses'),
        ),
        migrations.AlterField(
            model_name='class_attendance',
            name='coursesId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Courses'),
        ),
        migrations.AlterField(
            model_name='course_details',
            name='coursesId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Courses'),
        ),
        migrations.AlterField(
            model_name='democlass',
            name='coursesId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Courses'),
        ),
        migrations.AlterField(
            model_name='democlass_otp',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 19, 8, 17, 4, 131229, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='helpdesk',
            name='coursesId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Courses'),
        ),
        migrations.AlterField(
            model_name='intermediate',
            name='coursesId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Courses'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(upload_to='pics'),
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
