# Generated by Django 3.1.7 on 2021-04-30 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_stamp', '0045_auto_20210430_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='sub_category',
            field=models.CharField(max_length=150, unique=True, verbose_name='Sub Category'),
        ),
    ]
