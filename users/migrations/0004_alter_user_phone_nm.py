# Generated by Django 3.2.9 on 2021-11-13 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_profile_related_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_nm',
            field=models.CharField(max_length=11),
        ),
    ]