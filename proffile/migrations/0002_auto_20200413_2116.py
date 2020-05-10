# Generated by Django 3.0.2 on 2020-04-13 20:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('proffile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='date_joinded',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2020, 4, 13, 20, 16, 18, 718872, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='link',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]