# Generated by Django 3.2.9 on 2021-11-13 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20211113_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='jobs',
            field=models.ManyToManyField(blank=True, default=None, null=True, related_name='jobs', to='users.Job'),
        ),
    ]
