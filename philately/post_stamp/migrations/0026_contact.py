# Generated by Django 3.1.7 on 2021-04-27 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_stamp', '0025_auto_20210419_0944'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=200)),
                ('lastName', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=200)),
                ('content', models.TextField(max_length=1500)),
                ('dateSent', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
