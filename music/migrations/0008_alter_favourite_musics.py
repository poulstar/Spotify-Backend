# Generated by Django 3.2.7 on 2021-09-12 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0007_auto_20210911_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favourite',
            name='musics',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='is_fav', to='music.music'),
        ),
    ]
