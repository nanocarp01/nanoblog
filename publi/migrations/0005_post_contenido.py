# Generated by Django 4.2.7 on 2023-11-11 18:44

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publi', '0004_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='contenido',
            field=ckeditor.fields.RichTextField(default=3, verbose_name='Contenido'),
            preserve_default=False,
        ),
    ]
