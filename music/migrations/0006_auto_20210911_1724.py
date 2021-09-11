# Generated by Django 3.2.7 on 2021-09-11 17:24

from django.db import migrations, models
import music.models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_alter_category_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='music',
            name='file',
            field=models.FileField(upload_to='musics/files', validators=[music.models.validate_file_extension]),
        ),
    ]
