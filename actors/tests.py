from django.test import TestCase
from django.urls import reverse
from .models import Actor
from datetime import date
from django.core.files.uploadedfile import SimpleUploadedFile


# Тесты для модели Actor
class ActorModelTest(TestCase):
    def setUp(self):
        self.actor = Actor.objects.create(
            name="Leonardo DiCaprio",
            bio="An American actor and film producer.",
            birth_date=date(1974, 11, 11),
            photo=SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        )

    def test_actor_creation(self):
        self.assertEqual(self.actor.name, "Leonardo DiCaprio")
        self.assertEqual(self.actor.bio, "An American actor and film producer.")
        self.assertEqual(self.actor.birth_date, date(1974, 11, 11))
        self.assertTrue(self.actor.photo)

    def test_actor_string_representation(self):
        self.assertEqual(str(self.actor), "Leonardo DiCaprio")


# Тесты для представления actor_detail
class ActorDetailViewTest(TestCase):
    def setUp(self):
        self.actor = Actor.objects.create(
            name="Leonardo DiCaprio",
            bio="An American actor and film producer.",
            birth_date=date(1974, 11, 11),
            photo=SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        )

    def test_actor_detail_view(self):
        url = reverse('actor_detail', args=[self.actor.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'actor_detail.html')
        self.assertContains(response, "Leonardo DiCaprio")
        self.assertContains(response, "An American actor and film producer.")