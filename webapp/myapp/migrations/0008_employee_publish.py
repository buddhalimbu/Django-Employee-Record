# Generated by Django 3.1.1 on 2020-09-20 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20200920_2144'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='publish',
            field=models.BooleanField(default=True),
        ),
    ]
