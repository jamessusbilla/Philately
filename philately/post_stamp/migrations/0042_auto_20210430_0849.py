# Generated by Django 3.1.7 on 2021-04-30 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_stamp', '0041_auto_20210430_0837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='slug',
            field=models.SlugField(help_text='Key Code can be anywords you like but without spaces.', max_length=200, null=True, verbose_name='Key Code'),
        ),
    ]
