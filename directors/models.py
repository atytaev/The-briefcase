from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    birth_date = models.DateField()
    photo = models.ImageField(upload_to='director_photos/')

    def __str__(self):
        return self.name