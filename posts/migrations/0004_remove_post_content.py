# Generated by Django 5.0.6 on 2024-05-21 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
    ]