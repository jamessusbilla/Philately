# Generated by Django 3.1.7 on 2021-04-18 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post_stamp', '0021_delete_postalimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostalImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postalImage', models.FileField(upload_to='images/')),
                ('postal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='post_stamp.postal')),
            ],
        ),
    ]