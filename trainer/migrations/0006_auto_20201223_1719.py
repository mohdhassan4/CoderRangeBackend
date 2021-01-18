# Generated by Django 3.0.8 on 2020-12-23 11:49

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0066_auto_20201223_1719'),
        ('trainer', '0005_auto_20201216_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainercourse',
            name='coaching_courseid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Courses'),
        ),
        migrations.CreateModel(
            name='discussion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course_RandomId', models.CharField(max_length=150)),
                ('Text', models.TextField()),
                ('date', models.DateField(default=datetime.datetime(2020, 12, 23, 11, 49, 17, 209797, tzinfo=utc))),
                ('TrainerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]