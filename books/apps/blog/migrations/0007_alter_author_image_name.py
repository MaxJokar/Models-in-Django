# Generated by Django 4.0 on 2022-01-12 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_author_image_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='image_name',
            field=models.CharField(blank='True', default='', max_length=200, null=True),
        ),
    ]
