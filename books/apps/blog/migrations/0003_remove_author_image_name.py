# Generated by Django 4.0 on 2022-01-11 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_author_image_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='image_name',
        ),
    ]
