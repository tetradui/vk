# Generated by Django 5.0.6 on 2024-05-20 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='posts_img/', verbose_name='Изображение'),
        ),
    ]
