# Generated by Django 3.1.7 on 2021-04-27 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_stamp', '0029_auto_20210427_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='slug',
            field=models.SlugField(max_length=200, null=True, verbose_name='subject'),
        ),
    ]