# Generated by Django 4.2.2 on 2023-07-13 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0003_alter_movie_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='gallery'),
        ),
    ]
