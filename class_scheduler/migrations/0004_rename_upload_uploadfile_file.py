# Generated by Django 4.1.2 on 2022-10-08 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('class_scheduler', '0003_alter_uploadfile_upload'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uploadfile',
            old_name='upload',
            new_name='file',
        ),
    ]
