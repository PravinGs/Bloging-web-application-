# Generated by Django 3.1.3 on 2021-04-10 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0005_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(default='anonymoususer', max_length=40),
        ),
    ]