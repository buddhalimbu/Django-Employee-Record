# Generated by Django 3.1.1 on 2020-09-21 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_auto_20200921_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='ejoin',
            field=models.DateField(null=True),
        ),
    ]
