# Generated by Django 3.1.1 on 2020-09-23 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_auto_20200922_2020'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='epicture',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
