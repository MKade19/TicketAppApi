# Generated by Django 5.0.3 on 2024-07-25 15:55

import images.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to=images.models.upload_to),
        ),
    ]