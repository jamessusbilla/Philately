# Generated by Django 3.1.7 on 2021-04-16 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post_stamp', '0011_auto_20210416_1358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategory',
            name='distinguish_name',
        ),
    ]
