# Generated by Django 4.2.4 on 2023-08-27 20:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bulletin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=63, verbose_name='Заголовок')),
                ('content', models.TextField(default='Место для текста', verbose_name='Текст объявления')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63, unique=True, verbose_name='Имя категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_in', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('reply', models.CharField(max_length=255, verbose_name='Отклик')),
                ('is_accept', models.BooleanField(default=False, verbose_name='Принят')),
                ('bulletin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.bulletin', verbose_name='Объявление')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Отклик',
                'verbose_name_plural': 'Отклики',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='bulletin',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.category', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='bulletin',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
    ]
