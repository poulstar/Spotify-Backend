# Generated by Django 3.2.7 on 2021-09-12 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0008_alter_favourite_musics'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favourite',
            old_name='musics',
            new_name='music',
        ),
    ]
