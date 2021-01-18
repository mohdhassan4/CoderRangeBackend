# Generated by Django 3.0.8 on 2020-12-01 09:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0020_forgot_otp_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parent',
            name='country',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='parent',
            name='kid_age',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='parent',
            name='kidname',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='parent',
            name='lapptop_availability',
            field=models.CharField(blank=True, max_length=3),
        ),
        migrations.AlterField(
            model_name='parent',
            name='parent_name',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='parent',
            name='phonenumber',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=35, unique=True, verbose_name='email')),
                ('Trainername', models.CharField(blank=True, max_length=25)),
                ('Course_age', models.CharField(blank=True, max_length=15)),
                ('phonenumber', models.CharField(blank=True, max_length=15)),
                ('timing_availability', models.CharField(blank=True, max_length=50)),
                ('TrainerId', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
