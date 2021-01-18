# Generated by Django 3.0.8 on 2020-08-30 02:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0006_auto_20200827_1314'),
    ]

    operations = [
        migrations.CreateModel(
            name='projectviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Views', models.IntegerField(default=0)),
            ],
        ),
        migrations.RenameField(
            model_name='userprojects',
            old_name='Downloads',
            new_name='Rating',
        ),
        migrations.AddField(
            model_name='courses',
            name='course_BG_img',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='courses',
            name='From_age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='courses',
            name='Projectscount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='courses',
            name='To_age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='courses',
            name='courseImg',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='Messages',
        ),
        migrations.AddField(
            model_name='projectviews',
            name='ProjectId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.UserProjects'),
        ),
        migrations.AddField(
            model_name='projectviews',
            name='UserId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
