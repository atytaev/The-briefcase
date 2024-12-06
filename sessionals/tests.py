from datetime import date, timedelta

from django.test import TestCase
from django.urls import reverse
from django.utils.timezone import now

from films.models import Film
from users.models import User
from .models import Sessionals


class SessionViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.film = Film.objects.create(
            title="Test Film",
            description="Test Description",
            poster="test_poster.jpg",
            release_date=date(2022, 1, 1),
            duration=timedelta(minutes=120)# Указываем значение release_date
        )


        self.session1 = Sessionals.objects.create(
            film=self.film,
            start_time=now(),
            hall="Hall 1",
            available_seats=100
        )

        self.session2 = Sessionals.objects.create(
            film=self.film,
            start_time=now(),
            hall="Hall 2",
            available_seats=50
        )

    def test_session_list_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('session_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'session_list.html')
        self.assertIn(self.film, response.context['films'])
        self.assertIn(self.session1, response.context['sessions'])
        self.assertIn(self.session2, response.context['sessions'])

    def test_session_list_with_date_filter(self):
        self.client.login(username='testuser', password='testpassword')

        today = now().date()
        response = self.client.get(reverse('session_list'), {'date': today})
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.session1, response.context['sessions'])
        self.assertIn(self.session2, response.context['sessions'])

    def test_session_detail_view(self):
        response = self.client.get(reverse('session_detail', args=[self.session1.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'session_detail.html')
        self.assertEqual(response.context['session'], self.session1)