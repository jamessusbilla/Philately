# Generated by Django 3.1.7 on 2021-04-30 12:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_stamp', '0044_auto_20210430_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='history',
            name='datePosted',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Date Posted'),
        ),
        migrations.AlterField(
            model_name='links',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='postal',
            name='datePosted',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Date Posted'),
        ),
        migrations.AlterField(
            model_name='postalimage',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
