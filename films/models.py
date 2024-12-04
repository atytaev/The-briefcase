from django.db import models

class Film(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    genre = models.ManyToManyField('genres.Genre')  # ссылаемся на модель Genre из app 'genres'
    director = models.ForeignKey('directors.Director', on_delete=models.SET_NULL, null=True)  # ссылаемся на модель Director из app 'directors'
    actors = models.ManyToManyField('actors.Actor')  # ссылаемся на модель Actor из app 'actors'
    poster = models.ImageField(upload_to='film_posters/')
    duration = models.DurationField()

    def __str__(self):
        return self.title