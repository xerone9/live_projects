# Generated by Django 4.1.2 on 2022-10-08 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class_scheduler', '0002_uploadfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='upload',
            field=models.FileField(upload_to='uploads/'),
        ),
    ]
