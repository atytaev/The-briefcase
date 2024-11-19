from django.db import models
from django.utils import timezone
from django.urls import reverse
class Blog(models.Model):
    title = models.CharField(max_length=80)
    publication_year = models.PositiveSmallIntegerField()
    content = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(default=timezone.now)

    author = models.ForeignKey(
        'author.Author', on_delete=models.PROTECT,
        related_name='blogs',
        help_text='Author of the blog',
    )

    def __str__(self):
        return f'{self.title} ({self.publication_year})'


    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class Users(models.Model):
    username = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    def __str__(self):
        return f'{self.surname} {self.username}'

