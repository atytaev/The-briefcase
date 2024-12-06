from django.db import models


class Sessionals(models.Model):
    film = models.ForeignKey('films.Film', on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    hall = models.CharField(max_length=100)
    available_seats = models.IntegerField()

    def __str__(self):
        return f"{self.film.title} at {self.start_time}"
