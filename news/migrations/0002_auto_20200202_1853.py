# Generated by Django 3.0.2 on 2020-02-02 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='catid',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='news',
            name='catname',
            field=models.CharField(default='-', max_length=100),
        ),
        migrations.AddField(
            model_name='news',
            name='show',
            field=models.IntegerField(default=0),
        ),
    ]