# Generated by Django 3.1.1 on 2020-09-20 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20200920_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='staff_password',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='staff_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]