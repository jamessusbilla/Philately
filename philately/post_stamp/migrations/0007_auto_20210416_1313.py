# Generated by Django 3.1.7 on 2021-04-16 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_stamp', '0006_postal_sub_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postal',
            name='postTitle',
            field=models.CharField(max_length=150),
        ),
    ]
