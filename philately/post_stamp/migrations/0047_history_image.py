# Generated by Django 3.1.7 on 2021-04-30 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_stamp', '0046_auto_20210430_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='image',
            field=models.FileField(null=True, upload_to='images/', verbose_name='Upload Image'),
        ),
    ]
