# Generated by Django 5.1 on 2024-11-04 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_rename_finishes_count_userprofile_finishes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='finishes',
            new_name='finishes_count',
        ),
    ]
