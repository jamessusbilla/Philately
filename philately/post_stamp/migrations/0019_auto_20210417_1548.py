# Generated by Django 3.1.7 on 2021-04-17 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_stamp', '0018_auto_20210417_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postal',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.DeleteModel(
            name='PostalImages',
        ),
    ]
