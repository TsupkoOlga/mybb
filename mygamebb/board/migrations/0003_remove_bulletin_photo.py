# Generated by Django 4.2.4 on 2023-09-17 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_alter_bulletin_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bulletin',
            name='photo',
        ),
    ]
