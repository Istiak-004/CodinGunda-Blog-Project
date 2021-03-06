# Generated by Django 3.0.5 on 2020-04-24 21:15

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_subscribe'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body_text',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
