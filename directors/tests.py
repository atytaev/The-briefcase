from django.test import TestCase
from datetime import date
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Director
from django.urls import reverse

class DirectorModelTest(TestCase):
    def setUp(self):
        self.director = Director.objects.create(
            name="Quentin Tarantino",
            bio="An American filmmaker known for Pulp Fiction.",
            birth_date=date(1963, 3, 27),
            photo=SimpleUploadedFile("test_photo.jpg", b"file_content", content_type="image/jpeg")
        )

    def test_director_creation(self):
        self.assertEqual(self.director.name, "Quentin Tarantino")
        self.assertEqual(self.director.bio, "An American filmmaker known for Pulp Fiction.")
        self.assertEqual(self.director.birth_date, date(1963, 3, 27))
        self.assertTrue(self.director.photo)

    def test_string_representation(self):
        self.assertEqual(str(self.director), "Quentin Tarantino")

class DirectorDetailViewTest(TestCase):
    def setUp(self):
        self.director = Director.objects.create(
            name="Quentin Tarantino",
            bio="An American filmmaker known for Pulp Fiction.",
            birth_date=date(1963, 3, 27),
            photo=SimpleUploadedFile("test_photo.jpg", b"file_content", content_type="image/jpeg")
        )

    def test_director_detail_view(self):
        url = reverse('director_detail', args=[self.director.pk])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'director_detail.html')

        self.assertContains(response, "Quentin Tarantino")
        self.assertContains(response, "An American filmmaker known for Pulp Fiction.")