# Generated by Django 3.2 on 2021-04-09 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default='Anonymoususer', max_length=20, unique=True)),
                ('title', models.TextField()),
                ('context', models.TextField()),
                ('date_created', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
