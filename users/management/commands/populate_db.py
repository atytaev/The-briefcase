import random
from datetime import timedelta, datetime
from io import BytesIO

import requests
from django.core.files.images import ImageFile
from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
from cinema.settings import TMDB_API_KEY

from actors.models import Actor
from directors.models import Director
from films.models import Film
from genres.models import Genre
from sessionals.models import Sessionals
from ticket.models import Ticket
from users.models import User

fake = Faker()


class Command(BaseCommand):
    help = 'Заполняет базу данных фиктивными данными'

    def handle(self, *args, **kwargs):
        self.populate_actors()
        self.populate_directors()
        self.populate_genres()
        self.populate_films()
        self.populate_sessions()
        self.populate_users()
        self.populate_tickets()
        self.stdout.write(self.style.SUCCESS('База данных успешно заполнена!'))

    def fetch_image_from_tmdb(self, tmdb_id):
        """Функция для получения изображения через API TMDb"""
        url = f'https://api.themoviedb.org/3/person/{tmdb_id}/images?api_key={TMDB_API_KEY}'
        response = requests.get(url).json()
        try:
            # Получаем первое изображение (если доступно)
            profile_image_url = f'https://image.tmdb.org/t/p/original{response["profiles"][0]["file_path"]}'
            return profile_image_url
        except (KeyError, IndexError):
            return None

    def fetch_movie_poster_from_tmdb(self, tmdb_movie_id):
        """Функция для получения постера фильма через API TMDb"""
        url = f'https://api.themoviedb.org/3/movie/{tmdb_movie_id}/images?api_key={TMDB_API_KEY}'
        response = requests.get(url).json()
        try:
            # Получаем первое изображение постера фильма (если доступно)
            poster_path = response["posters"][0]["file_path"]
            poster_url = f'https://image.tmdb.org/t/p/original{poster_path}'
            return poster_url
        except (KeyError, IndexError):
            return None

    def populate_actors(self, n=10):
        for _ in range(n):
            actor = Actor(
                name=fake.name(),
                bio=fake.text(),
                birth_date=fake.date_of_birth(minimum_age=20, maximum_age=70)
            )

            # Получаем случайный ID актера (можно создать логику выбора)
            tmdb_actor_id = random.randint(1, 5000)  # Здесь должен быть реальный ID
            image_url = self.fetch_image_from_tmdb(tmdb_actor_id) or f'https://picsum.photos/400/400?random={random.randint(1, 1000)}'

            response = requests.get(image_url)
            actor_photo = BytesIO(response.content)
            actor.photo.save(f'{actor.name}_photo.jpg', ImageFile(actor_photo), save=True)

            actor.save()
            self.stdout.write(self.style.SUCCESS(f'Актер "{actor.name}" успешно сгенерирован!'))

    def populate_directors(self, n=5):
        for _ in range(n):
            director = Director(
                name=fake.name(),
                bio=fake.text(),
                birth_date=fake.date_of_birth(minimum_age=30, maximum_age=80)
            )

            # Получаем случайный ID режиссера (можно создать логику выбора)
            tmdb_director_id = random.randint(1, 5000)  # Здесь должен быть реальный ID
            image_url = self.fetch_image_from_tmdb(tmdb_director_id) or f'https://picsum.photos/400/400?random={random.randint(1, 1000)}'

            response = requests.get(image_url)
            director_photo = BytesIO(response.content)
            director.photo.save(f'{director.name}_photo.jpg', ImageFile(director_photo), save=True)

            director.save()
            self.stdout.write(self.style.SUCCESS(f'Режиссер "{director.name}" успешно сгенерирован!'))

    def populate_genres(self, n=5):
        genres = ['Action', 'Comedy', 'Drama', 'Thriller', 'Horror', 'Romance', 'Sci-Fi']
        for genre in genres:
            Genre.objects.create(name=genre)
            self.stdout.write(self.style.SUCCESS(f'Жанр "{genre}" успешно сгенерирован!'))


    def populate_films(self, n=20):
        directors = Director.objects.all()
        actors = Actor.objects.all()
        genres = Genre.objects.all()

        for _ in range(n):
            film = Film(
                title=fake.sentence(nb_words=3),
                description=fake.text(),
                release_date=fake.date_this_century(),
                director=random.choice(directors),
                poster=fake.image_url(),
                duration=timedelta(hours=random.randint(1, 3), minutes=random.randint(0, 59))
            )

            # Получаем постер фильма через TMDb
            tmdb_movie_id = random.randint(1, 5000)  # Здесь должен быть реальный ID фильма
            poster_url = self.fetch_movie_poster_from_tmdb(
                tmdb_movie_id) or f'https://picsum.photos/800/600?random={random.randint(1, 1000)}'

            response = requests.get(poster_url)
            film_poster = BytesIO(response.content)
            film.poster.save(f'{film.title}_poster.jpg', ImageFile(film_poster), save=True)

            film.save()
            film.genre.set(random.sample(list(genres), 2))  # Назначаем случайные жанры
            film.actors.set(random.sample(list(actors), 3))  # Назначаем случайных актеров

            self.stdout.write(self.style.SUCCESS(f'Фильм "{film.title}" успешно сгенерирован!'))

    def populate_sessions(self, n=10):
        films = Film.objects.all()
        today = datetime.now()
        for _ in range(n):
            session_date = today + timedelta(days=random.randint(0, 30))  # дата в пределах следующего месяца
            session_time = timezone.make_aware(session_date.replace(hour=random.randint(10, 22), minute=random.randint(0, 59)))

            session = Sessionals(
                film=random.choice(films),
                start_time=session_time,
                hall=fake.word(),
                available_seats=50
            )
            session.save()
            self.stdout.write(self.style.SUCCESS(f'Сеанс для фильма "{session.film.title}" успешно сгенерирован!'))

    def populate_users(self, n=10):
        for _ in range(n):
            user = User.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                password=fake.password()
            )

            # Генерация и сохранение фото профиля пользователя
            image_url = f'https://picsum.photos/400/400?random={random.randint(1, 1000)}'
            response = requests.get(image_url)
            user_profile_picture = BytesIO(response.content)
            user.profile_picture.save(f'{user.username}_profile.jpg', ImageFile(user_profile_picture), save=True)

            user.birth_date = fake.date_of_birth(minimum_age=18, maximum_age=80)
            user.phone_number = fake.phone_number()[:15]
            user.save()

            self.stdout.write(self.style.SUCCESS(f'Пользователь "{user.username}" успешно сгенерирован!'))

    def populate_tickets(self, n=30):
        sessions = Sessionals.objects.all()
        users = User.objects.all()

        for _ in range(n):
            ticket = Ticket(
                session=random.choice(sessions),
                user=random.choice(users),
                seat_number=random.randint(1, 50)
            )
            ticket.save()
            self.stdout.write(self.style.SUCCESS(f'Билет для сеанса "{ticket.session.film.title}" успешно сгенерирован!'))