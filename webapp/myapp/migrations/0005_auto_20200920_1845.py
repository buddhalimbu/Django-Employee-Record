# Generated by Django 3.1.1 on 2020-09-20 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20200920_1711'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='staff_goodname',
            new_name='goodname',
        ),
        migrations.RenameField(
            model_name='staff',
            old_name='staff_joined',
            new_name='joined_date',
        ),
        migrations.RenameField(
            model_name='staff',
            old_name='staff_name',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='staff',
            old_name='staff_picture',
            new_name='profile_pic',
        ),
        migrations.RenameField(
            model_name='staff',
            old_name='staff_password',
            new_name='username',
        ),
    ]
