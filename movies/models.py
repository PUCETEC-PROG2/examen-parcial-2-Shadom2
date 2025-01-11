from django.db import models

class Movie(models.Model):
    GENRE_CHOICES = [
        ('ACTION', 'Acción'),
        ('COMEDY', 'Comedia'),
        ('DRAMA', 'Drama'),
        ('HORROR', 'Terror'),
        ('SCI-FI', 'Ciencia Ficción'),
        ('ROMANCE', 'Romance'),
    ]

    title = models.CharField(max_length=100)
    genre = models.CharField(
        max_length=50,
        choices=GENRE_CHOICES,
    )
    director = models.CharField(max_length=100)
    release_year = models.IntegerField()
    synopsis = models.TextField()

    def __str__(self):
        return self.title