# Generated by Django 3.1.7 on 2021-04-16 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_stamp', '0002_auto_20210416_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postalcategory',
            name='post_category',
            field=models.CharField(blank=True, max_length=150, null=True, unique=True),
        ),
    ]
