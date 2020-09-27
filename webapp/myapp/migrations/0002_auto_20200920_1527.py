# Generated by Django 3.1.1 on 2020-09-20 09:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_name', models.CharField(max_length=100, null=True)),
                ('staff_picture', models.ImageField(upload_to='images')),
                ('staff_joined', models.DateField(default=datetime.date.today)),
                ('staff_goodname', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='employee',
            name='eemail',
        ),
        migrations.AddField(
            model_name='employee',
            name='ejoin',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
