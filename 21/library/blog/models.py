from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=80)
    publication_year = models.PositiveSmallIntegerField()

    author = models.ForeignKey(
        'author.Author', on_delete=models.PROTECT,
        related_name='blogs',
        help_text='Author of the blog',
    )

    def __str__(self):
        return f'{self.title} ({self.publication_year})'

class Users(models.Model):
    username = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    def __str__(self):
        return f'{self.surname} {self.username}'
