# Generated by Django 3.1.7 on 2021-05-03 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post_stamp', '0048_contact_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ('-date',)},
        ),
    ]
