# Generated by Django 4.0 on 2022-01-12 09:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_remove_author_email_remove_author_image_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='author',
            name='image_name',
            field=models.CharField(blank='True', max_length=200, null=True),
        ),
    ]