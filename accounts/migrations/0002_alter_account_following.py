# Generated by Django 3.2.7 on 2021-09-11 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_auto_20210911_1724'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='following',
            field=models.ManyToManyField(blank=True, to='music.Artist'),
        ),
    ]
