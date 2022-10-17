# Generated by Django 3.1.7 on 2021-04-27 22:34

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_stamp', '0030_auto_20210427_1202'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', ckeditor.fields.RichTextField()),
                ('slug', models.CharField(max_length=200, verbose_name='Greetings')),
                ('datePosted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
