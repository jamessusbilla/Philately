# Generated by Django 3.1.7 on 2021-04-28 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_stamp', '0033_auto_20210428_0119'),
    ]

    operations = [
        migrations.AddField(
            model_name='links',
            name='slug',
            field=models.SlugField(max_length=200, null=True, verbose_name='code'),
        ),
    ]
