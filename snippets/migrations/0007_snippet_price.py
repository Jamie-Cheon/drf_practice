# Generated by Django 3.0.7 on 2020-06-10 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0006_auto_20200610_0627'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
