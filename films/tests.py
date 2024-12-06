from datetime import date, timedelta

from django.test import TestCase
from django.urls import reverse

from actors.models import Actor
from directors.models import Director
from films.models import Film
from genres.models import Genre


class FilmModelTest(TestCase):
    def setUp(self):
        # Создаем связанные модели
        self.genre = Genre.objects.create(name="Action")
        self.director = Director.objects.create(name="Christopher Nolan", birth_date="1970-07-30")
        self.actor = Actor.objects.create(name="Leonardo DiCaprio", bio="Famous actor", birth_date=date(1974, 11, 11))

        # Создаем фильм
        self.film = Film.objects.create(
            title="Inception",
            description="A mind-bending thriller",
            release_date=date(2010, 7, 16),
            director=self.director,
            poster="test_poster.jpg",
            duration=timedelta(hours=2, minutes=28)
        )
        self.film.genre.add(self.genre)  # Добавляем жанр через M2M связь
        self.film.actors.add(self.actor)
    def test_film_creation(self):
        self.assertEqual(self.film.title, "Inception")
        self.assertEqual(self.film.description, "A mind-bending thriller")
        self.assertEqual(self.film.release_date, date(2010, 7, 16))
        self.assertEqual(self.film.director.name, "Christopher Nolan")
        self.assertEqual(self.film.poster, "test_poster.jpg")
        self.assertEqual(self.film.duration, timedelta(hours=2, minutes=28))

    def test_film_relations(self):
        self.assertIn(self.genre, self.film.genre.all())
        self.assertIn(self.actor, self.film.actors.all())

    def test_string_representation(self):
        self.assertEqual(str(self.film), "Inception")

class FilmListViewTest(TestCase):
    def setUp(self):
        self.genre = Genre.objects.create(name="Action")
        self.film1 = Film.objects.create(
            title="Inception",
            description="A mind-bending thriller",
            release_date=date(2010, 7, 16),
            poster="test_poster.jpg",
            duration=timedelta(hours=2, minutes=28)
        )
        self.film1.genre.add(self.genre)

        self.film2 = Film.objects.create(
            title="Interstellar",
            description="A journey through space and time",
            release_date=date(2014, 11, 7),
            poster="test_poster_2.jpg",
            duration=timedelta(hours=2, minutes=49)
        )

    def test_film_list_view(self):
        url = reverse('film_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'film_list.html')
        self.assertContains(response, "Inception")
        self.assertContains(response, "Interstellar")

    def test_film_list_filter_by_title(self):
        url = reverse('film_list') + '?title=Inception'
        response = self.client.get(url)
        self.assertContains(response, "Inception")
        self.assertNotContains(response, "Interstellar")

class FilmDetailViewTest(TestCase):
    def setUp(self):
        self.genre = Genre.objects.create(name="Action")
        self.film = Film.objects.create(
            title="Inception",
            description="A mind-bending thriller",
            release_date=date(2010, 7, 16),
            poster="test_poster.jpg",
            duration=timedelta(hours=2, minutes=28)
        )
        self.film.genre.add(self.genre)

    def test_film_detail_view(self):
        url = reverse('film_detail', args=[self.film.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'films_detail.html')
        self.assertContains(response, "Inception")
        self.assertContains(response, "A mind-bending thriller")