# Generated by Django 3.0.7 on 2020-06-10 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0007_snippet_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='published_on',
            field=models.BooleanField(default=False),
        ),
    ]