# Generated by Django 3.1.7 on 2021-04-16 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post_stamp', '0010_auto_20210416_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='distinguish_name',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='postal',
            name='category',
            field=models.IntegerField(choices=[(0, 'Telegrams'), (1, 'Post office at war'), (2, 'post office equipments'), (3, 'post office savings bank'), (4, 'postmarking machines'), (5, 'DateStamps'), (6, 'Stamp Dispensing Machines'), (7, 'Temporary Post Offices'), (8, 'Other post office history'), (9, 'NZ P & T IN WW1'), (10, 'FRANKING MACHINES'), (11, 'New Zealand'), (12, 'Non New Zealand')], default=0, help_text='the page where you would put the post'),
        ),
        migrations.AlterField(
            model_name='postal',
            name='sub_category',
            field=models.ForeignKey(blank=True, help_text='The Sub Category it is part of, if none, create one.', null=True, on_delete=django.db.models.deletion.CASCADE, to='post_stamp.subcategory'),
        ),
    ]
