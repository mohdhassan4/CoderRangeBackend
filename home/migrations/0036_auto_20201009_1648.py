# Generated by Django 3.0.8 on 2020-10-09 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0035_auto_20200929_1607'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beginner',
            name='coursesId',
        ),
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
            name='otp',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='helpdesk',
            name='coursesId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Courses'),
        ),
        migrations.AlterField(
            model_name='helpdesk',
            name='paymentid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Payment'),
        ),
        migrations.AlterField(
            model_name='intermediate',
            name='coursesId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Courses'),
        ),
        migrations.AlterField(
            model_name='payment',
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
        migrations.DeleteModel(
            name='ADVANCED',
        ),
        migrations.DeleteModel(
            name='BEGINNER',
        ),
    ]
