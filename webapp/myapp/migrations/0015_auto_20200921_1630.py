# Generated by Django 3.1.1 on 2020-09-21 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_auto_20200921_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='ejoin',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
