# Generated by Django 4.2.4 on 2023-09-18 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_alter_category_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bulletin',
            options={'ordering': ['-id'], 'verbose_name': 'Объявление', 'verbose_name_plural': 'Объявления'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
    ]