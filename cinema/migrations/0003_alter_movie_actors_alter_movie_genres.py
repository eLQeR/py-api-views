# Generated by Django 4.1 on 2024-02-24 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0002_actor_cinemahall_genre_movie_actors_movie_genres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(blank=True, null=True, related_name='movies', to='cinema.actor'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(blank=True, null=True, related_name='movies', to='cinema.genre'),
        ),
    ]
