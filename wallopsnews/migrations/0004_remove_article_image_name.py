# Generated by Django 2.0.6 on 2019-04-29 03:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallopsnews', '0003_article_image_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='image_name',
        ),
    ]
