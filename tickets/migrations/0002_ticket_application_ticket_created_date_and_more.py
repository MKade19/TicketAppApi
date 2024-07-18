# Generated by Django 5.0.3 on 2024-07-18 18:15

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_alter_event_price'),
        ('stadiums', '0001_initial'),
        ('tickets', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='application',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='events.application'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticket',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(1, 1, 1, 0, 0)),
        ),
        migrations.AddField(
            model_name='ticket',
            name='customer',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticket',
            name='is_sold',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ticket',
            name='seat',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='stadiums.seat'),
            preserve_default=False,
        ),
    ]