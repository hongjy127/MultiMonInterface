# Generated by Django 3.1.5 on 2021-02-15 10:33

from django.db import migrations
import photo.fields
import shopwindow.models


class Migration(migrations.Migration):

    dependencies = [
        ('shopwindow', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='image',
            field=photo.fields.ThumbnailImageField(blank=True, null=True, upload_to=shopwindow.models.review_image_path, verbose_name='IMAGE'),
        ),
    ]
