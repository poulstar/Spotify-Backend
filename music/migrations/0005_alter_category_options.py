# Generated by Django 3.2.7 on 2021-09-11 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_playlist_cover'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]