# Generated by Django 5.0.6 on 2024-05-21 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_user_bio_user_birth_date_user_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='pro_photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
