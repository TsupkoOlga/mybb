# Generated by Django 4.2.4 on 2023-09-22 16:29

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0005_alter_bulletin_options_alter_category_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=63, verbose_name='Заголовок')),
                ('time_in', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Текст новости')),
            ],
        ),
    ]
