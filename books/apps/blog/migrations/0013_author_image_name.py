# Generated by Django 4.0 on 2022-01-12 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_remove_author_image_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='image_name',
            field=models.CharField(blank='True', default='nophoto.png', max_length=200, null=True),
        ),
    ]
