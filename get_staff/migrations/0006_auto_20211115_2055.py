# Generated by Django 3.2.9 on 2021-11-15 20:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_staff', '0005_auto_20211115_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='c',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='commentgetstaff',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 15, 20, 55, 7, 130863), editable=False),
        ),
    ]
