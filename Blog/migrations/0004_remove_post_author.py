# Generated by Django 3.1.3 on 2021-04-10 01:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_auto_20210410_0724'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]
