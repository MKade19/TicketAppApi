# Generated by Django 5.0.3 on 2024-05-20 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roles', '0002_rename_permission_lounge_role_permission_hall_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='role',
            old_name='permission_staduum',
            new_name='permission_stadium',
        ),
    ]