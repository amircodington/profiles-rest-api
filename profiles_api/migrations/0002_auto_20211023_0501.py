# Generated by Django 2.2 on 2021-10-23 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='is_activate',
            new_name='is_active',
        ),
    ]
