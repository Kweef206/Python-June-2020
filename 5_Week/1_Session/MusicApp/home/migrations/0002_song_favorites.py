# Generated by Django 2.2.13 on 2020-07-07 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='favorites',
            field=models.ManyToManyField(related_name='favorite_songs', to='home.User'),
        ),
    ]
