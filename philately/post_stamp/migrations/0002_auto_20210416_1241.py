# Generated by Django 3.1.7 on 2021-04-16 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post_stamp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostalCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_category', models.CharField(max_length=150)),
            ],
        ),
        migrations.AlterField(
            model_name='postal',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post_stamp.postalcategory'),
        ),
    ]