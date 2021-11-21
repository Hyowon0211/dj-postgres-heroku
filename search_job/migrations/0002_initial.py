# Generated by Django 3.2.9 on 2021-11-22 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('search_job', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchjobpost',
            name='jobs',
            field=models.ManyToManyField(blank=True, to='users.Job'),
        ),
        migrations.AddField(
            model_name='searchjobpost',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
        migrations.AddField(
            model_name='commentsearchjob',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search_job.searchjobpost'),
        ),
        migrations.AddField(
            model_name='commentsearchjob',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
    ]