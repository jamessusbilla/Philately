# Generated by Django 3.1.7 on 2021-04-16 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post_stamp', '0003_auto_20210416_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postal',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='post_stamp.postalcategory'),
        ),
    ]
