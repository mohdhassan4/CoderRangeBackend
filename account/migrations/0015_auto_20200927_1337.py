# Generated by Django 3.0.8 on 2020-09-27 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_auto_20200927_1306'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parent',
            old_name='parentName',
            new_name='parent_name',
        ),
    ]