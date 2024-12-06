from django.db import models

class Film(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    genre = models.ManyToManyField('genres.Genre')
    director = models.ForeignKey('directors.Director', on_delete=models.SET_NULL, null=True)
    actors = models.ManyToManyField('actors.Actor')
    poster = models.ImageField(upload_to='film_posters/')
    duration = models.DurationField()

    def __str__(self):
        return self.title