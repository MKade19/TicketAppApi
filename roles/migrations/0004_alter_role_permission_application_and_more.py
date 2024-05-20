# Generated by Django 5.0.3 on 2024-05-20 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roles', '0003_rename_permission_staduum_role_permission_stadium'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='permission_application',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='role',
            name='permission_event',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='role',
            name='permission_hall',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='role',
            name='permission_seat',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='role',
            name='permission_stadium',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='role',
            name='permission_ticket',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='role',
            name='permission_user',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
