# Generated by Django 4.2.4 on 2023-09-17 16:18

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bulletin',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='Текст объявления'),
        ),
    ]
